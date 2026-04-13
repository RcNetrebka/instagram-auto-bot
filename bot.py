import json
import random
import requests
import os
import time

# -----------------------------------------
# 🔐 Tokens (GitHub Secrets)
# -----------------------------------------
INSTAGRAM_TOKEN = os.getenv("INSTAGRAM_TOKEN")
INSTAGRAM_BUSINESS_ID = os.getenv("INSTAGRAM_BUSINESS_ID")

# -----------------------------------------
# 📦 Carregar produtos
# -----------------------------------------
def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

# -----------------------------------------
# 🧠 Gerar legenda (mistura das duas versões)
# -----------------------------------------
def generate_caption(product):
    title = product["title"]
    link = product["link"]

    # ✅ frases de impacto (da versão nova)
    frases = [
        "🔥 OFERTA IMPERDÍVEL!",
        "💥 Corre que tá barato!",
        "🚨 Promoção por tempo limitado!",
        "💸 Preço que vale a pena!",
        "⚡ Aproveite antes que acabe!"
    ]

    frase = random.choice(frases)

    # ✅ estrutura profissional do estilo 4 (da versão antiga)
    caption = (
        f"{frase}\n\n"
        f"{title}\n\n"
        f"✅ Conforto e estilo\n"
        f"✅ Qualidade garantida\n"
        f"✅ Seleção especial SneakersRN\n\n"
        f"👉 Compre agora:\n{link}\n\n"
        f"👉 Mais ofertas e tênis em promoção:\n"
        f"https://collshp.com/ruannsneakers?view=storefront\n\n"
        f"#sneakers #tenis #promoção #ofertas #shopee #achadinhos #moda #estilo "
        f"#sneakersrn #tênismasculino #tênisfeminino"
    )

    return caption

# -----------------------------------------
# 📸 Postar no Instagram (API oficial)
# -----------------------------------------
def post_to_instagram(image_url, caption):
    create_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_BUSINESS_ID}/media"
    publish_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_BUSINESS_ID}/media_publish"

    print("📤 Enviando imagem...")

    create_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": INSTAGRAM_TOKEN
    }

    create_res = requests.post(create_url, data=create_payload).json()
    print("📩 Resposta criação:", create_res)

    creation_id = create_res.get("id")

    if not creation_id:
        print("❌ ERRO ao criar mídia:", create_res)
        return create_res

    # ✅ Espera obrigatória para o Instagram processar
    print("⏳ Aguardando processamento...")
    time.sleep(10)

    publish_payload = {
        "creation_id": creation_id,
        "access_token": INSTAGRAM_TOKEN
    }

    publish_res = requests.post(publish_url, data=publish_payload).json()
    print("📩 Resposta publicação:", publish_res)

    return publish_res

# -----------------------------------------
# 🚀 Executar bot (apenas 1 vez - GitHub Actions)
# -----------------------------------------
def run_bot():
    try:
        products = load_products()

        if not products:
            print("❌ Nenhum produto encontrado.")
            return

        product = random.choice(products)

        caption = generate_caption(product)
        image = product["image"]

        print("\n==============================")
        print("📸 Produto:", product["title"])
        print("🖼️ Imagem:", image)
        print("🔗 Link:", product["link"])
        print("==============================\n")

        result = post_to_instagram(image, caption)

        print("✅ Resultado final:", result)

    except Exception as e:
        print("❌ ERRO GERAL:", str(e))


# ✅ Roda 1 vez (GitHub Actions controla os horários)
if __name__ == "__main__":
    run_bot()
