from recognize import recognize_speech
# from speech_el import speak
from speech_local import speak_mac
from brain import ask_brain

def main():

    
    # speak("Hi, Welcome to Fords AI Assistant. Can I help you with something?", voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_multilingual_v2")
    speak_mac("Hi, Welcome to Fords AI Assistant. Can I help you with something?")

    
    user_input = recognize_speech()

    if user_input:
        print(f"User said: {user_input}")
        response = ask_brain(user_input)
        print(f"Brain response: {response}")
        # speak(response, voice_id="JBFqnCBsd6RMkjVDRZzb", model_id="eleven_multilingual_v2")
        speak_mac(response)
    else:
        print("No speech recognized.")


if __name__ == "__main__":
    main()