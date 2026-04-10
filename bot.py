import json
import random
import requests
import os

INSTAGRAM_TOKEN = os.getenv("INSTAGRAM_TOKEN")
INSTAGRAM_BUSINESS_ID = os.getenv("INSTAGRAM_BUSINESS_ID")

def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_caption(product):
    title = product["title"]
    link = product["link"]

    caption = (
        f"{title}\n\n"
        f"✨ Um dos nossos produtos mais desejados!\n"
        f"✅ Alta qualidade\n"
        f"✅ Ótimo custo-benefício\n"
        f"✅ Envio rápido\n\n"
        f"👉 Garanta o seu agora: {link}\n"
        f"#autocuidado #cuidadosdiarios #lojaonline #beleza #promoção"
    )

    return caption

def post_to_instagram(image_url, caption):
    create_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_BUSINESS_ID}/media"
    publish_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_BUSINESS_ID}/media_publish"

    create_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": INSTAGRAM_TOKEN
    }

    create_res = requests.post(create_url, data=create_payload).json()
    creation_id = create_res.get("id")

    publish_payload = {
        "creation_id": creation_id,
        "access_token": INSTAGRAM_TOKEN
    }

    publish_res = requests.post(publish_url, data=publish_payload).json()

    return publish_res

def run_bot():
    products = load_products()
    product = random.choice(products)

    caption = generate_caption(product)
    image = product["image"]

    result = post_to_instagram(image, caption)
    print("Publicado:", result)

if __name__ == "__main__":
    run_bot()
