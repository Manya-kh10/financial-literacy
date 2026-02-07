from gtts import gTTS
import os
import uuid

class TTSService:
    def generate_audio(self, text: str) -> str:
        """
        Generates audio from text and returns the file path.
        """
        # In a real microservice, you might want to clean up these files or serve from memory.
        # For simplicity, we save to a temporary file.
        filename = f"output_{uuid.uuid4()}.mp3"
        # Using a temp directory would be better
        filepath = os.path.join(os.path.dirname(__file__), "../", filename)
        
        tts = gTTS(text=text, lang='hi', slow=False)
        tts.save(filepath)
        
        return filepath
