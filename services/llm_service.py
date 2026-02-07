import os
import random
import json
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK_LLM", "true").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class LLMService:
    def __init__(self):
        # In a real scenario, initialize OpenAI client here
        self.dataset_path = os.path.join(os.path.dirname(__file__), "../data/dataset.json")
        try:
            with open(self.dataset_path, "r", encoding="utf-8") as f:
                self.dataset = json.load(f)
        except Exception as e:
            print(f"Error loading dataset: {e}")
            self.dataset = {"topics": {}}

    def get_chat_response(self, question: str) -> str:
        """
        Generates a chat response in simple Hindi using LLM or fallback.
        """
        # Simple keyword matching for context
        topic_key = None
        for key, value in self.dataset.get("topics", {}).items():
            if value["hindi_term"] in question or key in question.lower():
                topic_key = key
                break
        
        context = ""
        if topic_key:
            data = self.dataset["topics"][topic_key]
            context = f"Topic: {data['hindi_term']}. Definition: {data['description']} Example: {data['example']}"

        if USE_MOCK:
            return self._mock_chat_response(question, context)
        
        # Real LLM call would go here
        # return self._call_openai_chat(question, context)
        return self._mock_chat_response(question, context) # Fallback to mock for now if no key

    def _mock_chat_response(self, question: str, context: str) -> str:
        if not context:
            return "माफ करें, मैं केवल पैसे, बचत, बैंक और लोन के बारे में बता सकता हूँ।"
        
        # Construct a simple template-based response from the dataset
        return f"{context} जैसे कि, {self.dataset['topics'].get(list(self.dataset['topics'].keys())[0])['example']}"

    def get_quiz_response(self, topic: str) -> dict:
        """
        Generates a quiz for the given topic.
        """
        # Find the topic in dataset
        matched_topic = None
        for key, value in self.dataset.get("topics", {}).items():
            if key in topic.lower() or value["hindi_term"] in topic:
                matched_topic = key
                break
        
        if USE_MOCK:
            return self._mock_quiz_response(matched_topic)
            
        # Real LLM call would go here
        return self._mock_quiz_response(matched_topic)

    def _mock_quiz_response(self, topic_key: str) -> dict:
        if not topic_key:
             return {
                "questions": [
                    {
                        "q": "बचत करना क्यों जरूरी है?",
                        "options": ["भविष्य के लिए", "खर्च घटाने के लिए", "अमीर बनने के लिए", "दिखावे के लिए"],
                        "answer": "भविष्य के लिए"
                    }
                ]
            }

        data = self.dataset["topics"][topic_key]
        term = data["hindi_term"]
        desc = data["description"]
        
        # Generate a simple question based on the definition
        return {
            "questions": [
                {
                    "q": f"{term} क्या है?",
                    "options": [
                        "एक प्रकार का खाना",
                        "पैसे का लेन-देन", 
                        "घूमने की जगह",
                         desc.split(" ")[0] + "..." # Simplified distractor
                    ],
                    "answer": "पैसे का लेन-देन" # Placeholder logic, ideally more dynamic
                },
                 {
                    "q": f"हमें {term} का उपयोग कैसे करना चाहिए?",
                    "options": ["सोच-समझकर", "बेपरवाही से", "दोस्तों के साथ", "कभी नहीं"],
                    "answer": "सोच-समझकर"
                }

            ]
        }
