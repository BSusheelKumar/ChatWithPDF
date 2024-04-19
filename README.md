# Chat with PDF Using Gemini - Project Report

## Overview

This project aims to create a chat interface that allows users to ask questions from PDF documents. The backend processing is handled by Gemini, a conversational AI model, and the frontend is built using Streamlit.

## Technologies Used

- Streamlit: Used for building the frontend interface.
- PyPDF2: Used to extract text from PDF documents.
- langchain: A library for text processing and vectorization.
- GoogleGenerativeAI: A model for generating embeddings and conversational responses.
- FAISS: A library for similarity search and vector indexing.
- dotenv: Used for loading environment variables.
- Streamlit: Platform used for deployment.

## Functionality

The application allows users to upload PDF files containing text. It then extracts text from the PDF files, processes them into chunks, and creates a vector store using FAISS. Users can then ask questions related to the content of the PDF files, and Gemini provides responses based on the context.

## Deployment

The application is deployed using Streamlit, a Python library for creating web applications. The deployment enables users to access the chat interface through a web browser.

## Future Enhancements

Currently, the project focuses on extracting information and providing responses in the same language as the PDF documents. However, future plans include implementing translation capabilities to support translation from one language to another.

## Conclusion

The chat with PDF using Gemini project leverages advanced AI technologies to enable users to interact with PDF documents in a conversational manner. The deployment on Streamlit provides a user-friendly interface for accessing the application.
