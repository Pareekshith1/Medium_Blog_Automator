import os
import requests
from dotenv import load_dotenv
from typing import List, Tuple

load_dotenv()

# RapidAPI credentials
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "medium2.p.rapidapi.com"
BASE_URL = f"https://{RAPIDAPI_HOST}"

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

def upload_image_to_imgbb(image_file) -> str:
    """
    Uploads the image temporarily to imgbb.com for public URL use (free, no auth required).
    """
    IMGBB_API = "https://api.imgbb.com/1/upload"
    IMGBB_KEY = os.getenv("IMGBB_API_KEY")

    if not IMGBB_KEY:
        raise ValueError("🔐 Missing IMGBB_API_KEY in your .env file.")

    response = requests.post(
        IMGBB_API,
        data={"key": IMGBB_KEY},
        files={"image": image_file}
    )

    if response.status_code == 200:
        return response.json()["data"]["url"]
    else:
        raise Exception(f"❌ Failed to upload image to imgbb: {response.text}")

def format_html(paragraphs: List[str], images: List[Tuple[bytes, str]]) -> str:
    """
    Takes blog paragraphs and image byte tuples and returns formatted HTML.
    """
    html = ""
    for i, para in enumerate(paragraphs):
        html += f"<p>{para}</p>\n"
        if i < len(images):
            img_data, caption = images[i]
            image_url = upload_image_to_imgbb(img_data)
            html += f"<figure><img src='{image_url}' alt='Image'><figcaption>{caption}</figcaption></figure>\n"
    return html

def upload_blog(title: str, paragraphs: List[str], images: List[Tuple[bytes, str]], tags: List[str] = []):
    try:
        content = format_html(paragraphs, images)

        post_data = {
            "title": title,
            "contentFormat": "html",
            "content": content,
            "tags": tags,
            "publishStatus": "public"
        }

        url = f"https://{RAPIDAPI_HOST}/v1/users/me/posts"
        response = requests.post(url, headers=HEADERS, json=post_data)

        if response.status_code != 200:
            raise Exception(f"❌ Blog post failed: {response.status_code} - {response.text}")

        result = response.json()
        print("✅ Blog uploaded successfully!")
        print("🔗 URL:", result.get("data", {}).get("url", "Unknown"))
        return result.get("data")

    except Exception as e:
        print("❌ Error during blog upload:", str(e))
        return None
