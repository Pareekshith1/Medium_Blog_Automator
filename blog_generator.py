import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

api_url = "https://api.together.xyz/v1/chat/completions"
MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

def load_template() -> str:
    try:
        with open("templates/blog_prompt_template.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("Template not found. Please make sure the template exists.")

def generate_blog(prompt: str) -> str:
    if not TOGETHER_API_KEY:
        raise ValueError("TOGETHER_API_KEY not found in environment variables.")

    template = load_template()
    final_prompt = template.replace("{prompt}", prompt)

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    def call_llm(user_prompt: str):
        data = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": 
                "You are an expert SEO-focused blog writer and fact-checker."
                "Produce detailed, accurate, and engaging content with strong SEO."
                },
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 2048,
            "temperature": 0.7,
            "top_p": 0.9,
            "frequency_penalty": 0.2,
            "presence_penalty": 0.1,
        }

        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code != 200:
            raise Exception(f"Request Failed: {response.status_code} \n{response.text}")
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    # Step 1: Get initial blog
    blog_part = call_llm(final_prompt)

    # Step 2: Detect cutoff
    if blog_part.endswith(("...", ",", "and", "or", "to", "of", "the", "-", "with", "in", "for")):
        print("⚠️ Detected incomplete ending... requesting continuation.")
        continuation = call_llm("Continue the previous blog content.")
        return blog_part + "\n\n" + continuation

    return blog_part

# For unit test purpose only
if __name__ == "__main__":
    prompt = input("Enter your topic for the blog: ")
    generated_text = generate_blog(prompt)
    print("\nGenerated Blog:\n")
    print(generated_text)
