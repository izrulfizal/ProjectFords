import os

def speak_mac(text, voice="Samantha", rate=180):
    """
    Use macOS built-in `say` command to convert text to speech.

    Parameters:
        text (str): The text to be spoken.
        voice (str): macOS system voice (default: "Samantha").
        rate (int): Speaking rate (words per minute).
    """
    try:
        # Escape quotes to prevent shell errors
        safe_text = text.replace('"', '\\"')
        os.system(f'say -v "{voice}" -r {rate} "{safe_text}"')
    except Exception as e:
        print(f"❌ Error using macOS TTS: {e}")


# Example usage
if __name__ == "__main__":
    speak_mac("Hello! This is Nova using macOS built-in voice.")
