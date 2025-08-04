import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_brain(prompt, model="gemma2-9b-it"):
    """
    Sends a prompt to Groq LLM with a system message to enforce concise replies.
    
    Parameters:
        prompt (str): The user question.
        model (str): The LLM model to use.

    Returns:
        str: The assistant's short reply.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant for a university faculty. "
                        "Always respond with short and direct answers only. "
                        "Do not elaborate unless specifically asked to."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error in ask_brain(): {e}"

# Example usage
if __name__ == "__main__":
    reply = ask_brain("What is cloud computing?")
    print(reply)
