from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")


elevenlabs = ElevenLabs(api_key=api_key)

def speak(text, voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_multilingual_v2", output_path="Audio/speech.mp3"):
    """
    Convert text to speech using ElevenLabs streaming and play it.

    - text: The text to convert to speech
    - voice_id: Voice ID from ElevenLabs
    - model_id: Model ID for the voice (e.g., 'eleven_monolingual_v1', 'eleven_multilingual_v2')
    - output_path: Path to save the MP3 audio file
    """
    try:

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

 
        audio_stream = elevenlabs.text_to_speech.stream(
            text=text,
            voice_id=voice_id,
            model_id=model_id
        )

    
        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

    #  MacOS
        os.system(f"afplay {output_path}")
    #  Windows
        # os.system(f'start {output_path}')  

    except Exception as e:
        print(f"❌ Error in speak(): {e}")



if __name__ == "__main__":
    speak("Hi, can I help you with something?", voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_multilingual_v2")
