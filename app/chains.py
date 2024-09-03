import os
import textwrap
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from portfolio import Portfolio

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-70b-versatile"
        )
        self.portfolio = Portfolio()
        self.portfolio.load_portfolio()

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills`, and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links=None):
        job_description = job.get('description', '')
        skills = job.get('skills', [])

        # Query the portfolio for relevant resume links
        resume_links = self.portfolio.query_links(skills)

        # Format resume links for the email prompt
        formatted_resume_links = ", ".join(resume_links) if resume_links else "No links available"

        # Define the email prompt template
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are a job applicant writing a cold email to the HR department regarding the job described above. Your task is to compose a professional and compelling email that:

            1. Expresses your interest in the position
            2. Highlights your relevant skills and experience
            3. Demonstrates your knowledge of the job requirements
            4. Includes the following link(s) to your resume or portfolio: {resume_links}

            Keep the email concise, professional, and tailored to the specific job. Do not provide a preamble or mention any specific names. Do not include any closing phrases like "Best regards" or similar. End the email with the last relevant sentence.

            ### EMAIL (NO PREAMBLE, NO CLOSING PHRASE):
            """
        )

        # Create the email chain
        chain_email = prompt_email | self.llm

        # Generate the email
        res = chain_email.invoke({
            "job_description": job_description,
            "resume_links": formatted_resume_links
        })

        # Format the output to fit within a reasonable width
        wrapped_content = textwrap.fill(res.content, width=80)

        return wrapped_content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
