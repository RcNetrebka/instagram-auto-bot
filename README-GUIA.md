# BOT AUTOMÁTICO – Instagram @autocuidadoparavc

✅ Posta 2 produtos por dia (08h e 19h)  
✅ Gera legenda automática para vendas  
✅ Busca produtos da loja CollShp  
✅ Roda 100% na nuvem (GitHub Actions)  
✅ Sem necessidade de instalar nada no computador

---

## COMO FUNCIONA

1. scraper.py → coleta produtos da loja
2. bot.py → gera legenda e posta no Instagram
3. postador.yml → agenda as execuções automáticas
4. products.json → banco de dados dos produtos

---

## COMO CONFIGURAR AS CHAVES DO INSTAGRAM

Ir em:
`Settings → Secrets → Actions → New Repository Secret`

Criar dois segredos:

- **INSTAGRAM_TOKEN**
- **INSTAGRAM_BUSINESS_ID**

O bot usa esses dados para realizar a postagem automática.

---

## HORÁRIOS DAS POSTAGENS

- Todo dia às 08h
- Todo dia às 19h

Configuração feita em `.github/workflows/postador.yml`

---

## PRONTO!
Assim que os segredos forem adicionados, o bot começa a postar sozinho.
