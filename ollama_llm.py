
# ollama_llm.py
import subprocess

def call_mistral(text: str) -> str:
    """
    Call Ollama Mistral locally via CLI (UTF-8 safe, Windows compatible)
    """

    if not text or not text.strip():
        return "Sorry, I could not understand."

    try:
        # Run Ollama with UTF-8 safe input
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=text,
            capture_output=True,
            text=True,
            encoding="utf-8",   # 🔑 Fix Unicode (Hindi)
            errors="ignore",
            check=True
        )

        response = result.stdout.strip()

        if not response:
            return "Sorry, I could not generate a response."

        return response

    except subprocess.CalledProcessError as e:
        print("❌ Ollama runtime error:", e.stderr)
        return "Sorry, there was an error running the model."

    except FileNotFoundError:
        return "Ollama is not installed or not in PATH."

    except Exception as e:
        print("❌ Unexpected Ollama error:", e)
        return "Sorry, I could not process your request."
