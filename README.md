# Chat with PDF using Google Generative AI

This project allows users to interact with a PDF document by uploading it and asking questions related to its content. The app uses Google Generative AI (Gemini) to provide responses to user queries based on the context extracted from the PDF.

## Features

- **PDF Upload**: Users can upload a PDF file for interaction.
- **Text Extraction**: The app extracts text from the PDF, splits it into chunks, and indexes it for easy retrieval.
- **Chat with AI**: Users can ask questions about the uploaded PDF, and the AI model will generate responses based on the context of the document.
- **Session History**: The app keeps track of the chat history between the user and the AI.
  
## Technologies

- **Streamlit**: For building the web interface.
- **Google Generative AI (Gemini)**: For generating AI responses based on the document content.
- **LangChain**: For managing embeddings and vector stores, enabling context retrieval from the PDF.
- **FAISS**: A library for efficient similarity search.
- **PyPDF**: To extract text from PDF files.
- **Hugging Face**: For embeddings using pre-trained language models.
- **Python-dotenv**: To manage environment variables such as the API key.

## Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- Streamlit
- Google Generative AI API access
- Necessary Python libraries (see `requirements.txt`)

### Installation

Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/chat-with-pdf.git
