from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

import json

def test_chat():
    print("Testing /ai/chat...")
    response = client.post("/ai/chat", json={"question": "बचत क्या है?"})
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), ensure_ascii=True)}")
    assert response.status_code == 200
    assert "answer" in response.json()

def test_quiz():
    print("\nTesting /ai/quiz...")
    response = client.post("/ai/quiz", json={"topic": "बचत"})
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), ensure_ascii=True)}")
    assert response.status_code == 200
    assert "questions" in response.json()
    assert len(response.json()["questions"]) > 0

def test_tts():
    print("\nTesting /ai/tts...")
    response = client.post("/ai/tts", json={"text": "नमस्ते, यह एक परीक्षण है।"})
    print(f"Status: {response.status_code}")
    # Content-type should be audio/mpeg
    print(f"Content-Type: {response.headers['content-type']}")
    assert response.status_code == 200
    assert "audio" in response.headers["content-type"]

if __name__ == "__main__":
    try:
        test_chat()
        test_quiz()
        test_tts()
        print("\nAll tests passed!")
    except Exception as e:
        print(f"\nTest failed: {e}")
