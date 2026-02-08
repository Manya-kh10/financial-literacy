from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

import json

def test_chat():
    print("Testing /ai/chat...")
    
    # 1. Concept Learning
    q1 = "ब्याज क्या है?"
    print("\nQuery 1: What is Interest? (Hindi)")
    r1 = client.post("/ai/chat", json={"question": q1})
    print(f"Response: {json.dumps(r1.json(), ensure_ascii=True)}")
    assert r1.status_code == 200

    # 2. Transaction Guidance
    q2 = "यूपीआई से पैसे कैसे भेजें?"
    print("\nQuery 2: How to send money via UPI? (Hindi)")
    r2 = client.post("/ai/chat", json={"question": q2})
    print(f"Response: {json.dumps(r2.json(), ensure_ascii=True)}")
    assert r2.status_code == 200
    assert "1." in r2.json()["answer"] 

    # 3. Decision Support
    q3 = "क्या मुझे लोन लेना चाहिए?"
    print("\nQuery 3: Should I take a loan? (Hindi)")
    r3 = client.post("/ai/chat", json={"question": q3})
    print(f"Response: {json.dumps(r3.json(), ensure_ascii=True)}")
    assert r3.status_code == 200

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
