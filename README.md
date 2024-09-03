# Cold-Mail-Generator-using-Llama-3.1

## Overview

This project is a Cold Email Generator that utilizes the Llama 3.1 model to generate responses. Due to the computational intensity of Llama 3.1, GroqCloud is used to expedite the response generation process, leveraging its LPU technology for faster performance.

## Tools and Technologies

- **Llama 3.1**: A powerful language model with 70 billion parameters for generating responses.
- **GroqCloud**: Provides faster execution of the Llama model using its LPU technology.
- **Groq API Key**: 'your_api_key'
- **ChatGroq**: Utilizes the LangChain framework to interact with the Llama model.
- **ChromaDB**: A lightweight vector database used for storing and retrieving data efficiently.
- **LangChain**: Framework used for creating and managing language model chains.
- **WebBaseLoader**: For web scraping to gather and process data.
- **Pipellm**: For forming and managing chains to pass data to the language model.
- *Streamlit**: For the User Interface.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/VidhiyaSB/Cold-Mail-Generator-using-Llama-3.1.git
   cd Cold-Mail-Generator-using-Llama-3.1
### Configuration
Set Up GroqCloud:

Ensure you have access to GroqCloud and set up the API key. This key should be kept secure. You can set it in your environment variables or a configuration file.

Configure API Key:

Add your Groq API key to a configuration file or environment variable

### Run the Cold Email Generator:

### Execute the script to start generating cold emails:
streamlit run .\app\main.py
This script will use the Llama 3.1 model via GroqCloud and the LangChain framework to generate cold emails based on the input data.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For any questions or issues, please contact www.x.com/@VidhiyaSB.
