import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio1.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                techstack = row.get("Techstack", "")
                links = row.get("Links", "")
                if techstack and links:
                    # Assuming 'links' could be a single link or a comma-separated list of links
                    links_list = [link.strip() for link in links.split(',') if link.strip()]
                    self.collection.add(
                        documents=[techstack],
                        metadatas={"links": links_list},
                        ids=[str(uuid.uuid4())]
                    )

    def query_links(self, skills):
        if not isinstance(skills, list):
            skills = [skills]

        query_result = self.collection.query(query_texts=skills, n_results=2)
        metadatas = query_result.get('metadatas', [])
        resume_links = []
        
        for metadata_list in metadatas:
            for metadata in metadata_list:
                links = metadata.get('links', [])
                if isinstance(links, str):
                    links = links.split(',')
                resume_links.extend(link.strip() for link in links if link.strip())
        
        # Remove duplicates and empty strings
        resume_links = list(set(resume_links))
        return resume_links
