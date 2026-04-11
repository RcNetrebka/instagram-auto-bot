# 🤖 Bot Automático Instagram – SneakersRN.OFC

Este repositório contém um bot totalmente automatizado que publica **2 vezes por dia** no Instagram da loja **SneakersRN.OFC**, usando uma lista de produtos configurada no arquivo `products.json`.

O bot roda através do **GitHub Actions**, o que significa que:
✅ Não precisa rodar nada no PC  
✅ Funciona mesmo com PC travado  
✅ Executa sempre nos horários programados  

---

## 📌 COMO FUNCIONA

### ✅ 1. O arquivo `products.json`
Este arquivo contém todos os produtos que o bot pode postar.

Cada item segue este formato:

```json
{
  "title": "Nome do Produto",
  "link": "https://shopee.com.br/...",
  "image": "URL da Imagem"
}
