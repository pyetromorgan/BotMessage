import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL_PROJECT = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

url_contatos = f"{URL_PROJECT}/rest/v1/contatos"

url_zapi = os.getenv("ZAPI_CLIENT_TOKEN")

keyheader = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}"
}

response = requests.get(url_contatos, headers=keyheader)
contatos = response.json()

print("Status:", response.status_code)
print("Data:", response.json())

for contato in contatos:
    client_name = contato["nome"]
    client_phone = contato["telefone"]

    message_data = {
        "phone": client_phone,
        "message": f"Olá, {client_name} tudo bem com você?!"
    }

    print(f"enviando msg para {client_name}")

    send_reply = requests.post(url_zapi, json=message_data)

    if send_reply.status_code == 200:
        print(f"mensagem enviada para {client_name}")
    else:
        print(f"erro ao enviar mensagem para {client_name}")
        print(f"detalhes do erro: {send_reply.text}")