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

## Testing

Run the included test script to verify all endpoints:

```bash
python test_app.py
```
