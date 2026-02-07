from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
import os
import uvicorn
from contextlib import asynccontextmanager

# Import internal modules
from models.schemas import ChatRequest, ChatResponse, TTSRequest, QuizRequest, QuizResponse
from services.llm_service import LLMService
from services.tts_service import TTSService

# Initialize services
llm_service = LLMService()
tts_service = TTSService()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Load resources if needed
    print("Starting up AI Financial Literacy Microservice...")
    yield
    # Shutdown: Clean up temporary files if any
    print("Shutting down...")

app = FastAPI(
    title="Rural Finance AI Microservice",
    description="AI-based financial education for rural India using simple Hindi.",
    version="1.0.0",
    lifespan=lifespan
)

@app.post("/ai/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Get a simple Hindi answer to a financial question.
    """
    try:
        answer = llm_service.get_chat_response(request.question)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ai/tts")
async def tts_endpoint(request: TTSRequest, background_tasks: BackgroundTasks):
    """
    Convert Hindi text to speech. Returns an audio file.
    """
    try:
        file_path = tts_service.generate_audio(request.text)
        
        # Function to remove file after response is sent
        def remove_file(path: str):
            try:
                os.remove(path)
            except Exception:
                pass

        background_tasks.add_task(remove_file, file_path)
        return FileResponse(file_path, media_type="audio/mpeg", filename="speech.mp3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ai/quiz", response_model=QuizResponse)
async def quiz_endpoint(request: QuizRequest):
    """
    Generate a quiz on a financial topic.
    """
    try:
        quiz_data = llm_service.get_quiz_response(request.topic)
        # Transform raw dict to QuizResponse model if needed, but pydantic handles dicts well
        # We might need to map specific fields if the service returns slightly different structure
        # The current mock implementation returns exact structure.
        return QuizResponse(**quiz_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
