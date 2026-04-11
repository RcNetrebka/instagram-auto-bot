import json
import random
import requests
import os

# Tokens e IDs carregados do GitHub Secrets
INSTAGRAM_TOKEN = os.getenv("INSTAGRAM_TOKEN")
INSTAGRAM_BUSINESS_ID = os.getenv("INSTAGRAM_BUSINESS_ID")

# -----------------------------------------
# 1. Carregar lista de produtos
# -----------------------------------------
def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

# -----------------------------------------
# 2. Gerar legenda inteligente com estilo 4
# -----------------------------------------
def generate_caption(product):
    title = product["title"]
    link = product["link"]

    caption = (
        f"{title}\n\n"
        f"✅ Qualidade, conforto e estilo\n"
        f"✅ Seleção especial da SneakersRN\n"
        f"✅ Modelos atualizados diariamente\n\n"
        f"👉 Mais ofertas e tênis em promoção:\n"
        f"https://collshp.com/ruannsneakers?view=storefront\n\n"
        f"#sneakers #tenis #moda #ofertas #promoção #sneakersrn #tênisfeminino "
        f"#tênismasculino #corrida #academia #estilo #streetwear"
    )

    return caption

# -----------------------------------------
# 3. Postar no Instagram via API
# -----------------------------------------
def post_to_instagram(image_url, caption):
    create_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_BUSINESS_ID}/media"
    publish_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_BUSINESS_ID}/media_publish"

    # Criar o media object
    create_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": INSTAGRAM_TOKEN
    }

    create_res = requests.post(create_url, data=create_payload).json()
    creation_id = create_res.get("id")

    if not creation_id:
        print("❌ ERRO: Não foi possível criar o ID da imagem:", create_res)
        return create_res

    # Publicar
    publish_payload = {
        "creation_id": creation_id,
        "access_token": INSTAGRAM_TOKEN
    }

    publish_res = requests.post(publish_url, data=publish_payload).json()
    return publish_res

# -----------------------------------------
# 4. Rodar o bot
# -----------------------------------------
def run_bot():
    products = load_products()
    product = random.choice(products)

    caption = generate_caption(product)
    image = product["image"]

    print("📸 Postando produto:", product["title"])
    print("🖼️ Imagem:", image)
    print("🔗 Link:", product["link"])

    result = post_to_instagram(image, caption)
    print("✅ Publicado:", result)


if __name__ == "__main__":
    run_bot()
