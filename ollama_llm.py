
# ollama_llm.py

import subprocess

def call_mistral(user_query: str, schemes: list) -> str:
    context = ""
    for s in schemes:
        context += f"""
योजना: {s.get('name')}
विवरण: {s.get('description')}
पात्रता: {s.get('eligibility')}
लाभ: {s.get('benefits')}
\n
"""

    prompt = f"""
आप एक भारतीय कृषि सहायक AI हैं।
केवल नीचे दी गई सरकारी योजनाओं की जानकारी के आधार पर उत्तर दें।

{context}

किसान का प्रश्न:
{user_query}

सरल हिंदी में उत्तर दें।
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return result.stdout.strip()

    except Exception as e:
        print("❌ Ollama error:", e)
        return "माफ़ कीजिए, अभी उत्तर नहीं दे पा रहा हूँ।"

