# AI Microservice for Financial Literacy

This is a FastAPI-based microservice designed to provide financial literacy in rural India using simple Hindi.

## Features

- **Chat API (`/ai/chat`)**: Answers financial questions in simple Hindi (using LLM or internal dataset).
- **TTS API (`/ai/tts`)**: Converts Hindi text to audio (MP3).
- **Quiz API (`/ai/quiz`)**: Generates multiple-choice questions on financial topics.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    - Rename `.env` (already created) and add your `OPENAI_API_KEY` if you want to use real LLM responses.
    - Set `USE_MOCK_LLM=true` to use the built-in mock responses (default).

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once running, visit `http://localhost:8000/docs` for the interactive Swagger UI.


## Project Structure & File Guide

Here is a breakdown of the files in this repository:

- **`main.py`**: The heart of the application. It creates the FastAPI app and defines the API endpoints (`/ai/chat`, `/ai/tts`, `/ai/quiz`). It connects the web requests to the logic in the `services/` folder.
- **`services/llm_service.py`**: Contains the "brain" of the AI. It handles the logic for answering questions and generating quizzes. It includes a "Mock Mode" to work without an API key by using the internal dataset.
- **`services/tts_service.py`**: Handles Text-to-Speech conversion. It takes Hindi text and creates an MP3 file using Google's Text-to-Speech (gTTS) library.
- **`models/schemas.py`**: Defines the "shape" of the data. It ensures that requests and responses follow a strict format (e.g., a ChatRequest must have a "question" field).
- **`data/dataset.json`**: Acts as a small internal database. It contains simple Hindi definitions and examples for Money, Savings, Bank, and Loan.
- **`test_app.py`**: A test script to verify that the application is working correctly. It sends fake requests to your running app and checks the responses.
- **`requirements.txt`**: A list of all the Python libraries required to run this project (FastAPI, gTTS, OpenAI, etc.).
- **`.env`**: Stores sensitive settings like your API keys. **Never share this file.**
