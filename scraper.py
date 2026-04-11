import requests
from bs4 import BeautifulSoup
importruannsneakers?view=storefront"import json

def scrape_products():
    response = requests.get(STORE_URL, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    # Selecionar todos os produtos do storefront Collshp
    items = soup.select("a[href*='product']")
    for item in items:
        title = item.get_text(strip=True)
        link = item["href"]

        # Corrige link incompleto
        if not link.startswith("http"):
            link = "https://collshp.com" + link

        # Pega imagem do produto, quando disponível
        img_tag = item.find("img")
        img = img_tag["src"] if img_tag else ""

        products.append({
            "title": title,
            "link": link,
            "image": img
        })

    # Salvar arquivo
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    return products

if __name__ == "__main__":
    scrape_products()

# ✅ Loja nova SneakersRN
