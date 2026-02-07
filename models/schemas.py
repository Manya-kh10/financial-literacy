from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

class TTSRequest(BaseModel):
    text: str

class TTSResponse(BaseModel):
    # This might be binary or a path, but for Swagger documentation purposes, we might just return a file directly.
    # However, sometimes a JSON wrapper is useful if we return a URL.
    # The requirement says "Output: Hindi audio (MP3/WAV)", implying a file response.
    # But let's define a model for any metadata if needed, though FastAPI returns FileResponse directly.
    pass 

class QuizRequest(BaseModel):
    topic: str

class QuizQuestion(BaseModel):
    q: str
    options: List[str]
    answer: str

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
