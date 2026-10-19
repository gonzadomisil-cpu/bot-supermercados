import os
import requests

def enviar_telegram(texto):
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
    
    if not TOKEN or not CHAT_ID:
        print("Error: Faltan variables de entorno de Telegram")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={texto}"
    requests.get(url)

def main():
    mensaje = "🛒 Bot de supermercados funcionando correctamente!\n\nPróximamente compararemos precios reales."
    enviar_telegram(mensaje)
    print("Bot ejecutado con éxito")

if __name__ == "__main__":
    main()
