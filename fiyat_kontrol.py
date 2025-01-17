import requests
from bs4 import BeautifulSoup
from telegram import Bot


TELEGRAM_TOKEN = '7511449689:AAGjv-8FsXDDZ495PHem8FUR0_OWvwPKgNo' 
CHAT_ID = '1103239100' 

def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)
    print(f"Telegram mesajı gönderildi: {message}")

def urun_kontrol():
    URL="https://www.amazon.com.tr/Philips-XB7151-07-Marathon-PowerCyclone/dp/B0C7RGNNW2/ref=zg_bs_g_home_d_sccl_10/261-6035856-1003306?th=1"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
    
    sayfa = requests.get(URL, headers=headers)
    icerik = BeautifulSoup(sayfa.content, 'html.parser')

    urun_adi = icerik.find(id='productTitle').get_text()
    yeni_urun_adi = urun_adi[8:95]

    urun_ucreti = icerik.find(id='apex_desktop').get_text()

    yeni_ucret = int(urun_ucreti[17:22].replace('.', ''))

    if yeni_ucret < 8000:
        mesaj = f"{yeni_ucret} TL {yeni_urun_adi} fiyatı düştü, acele et!"
        send_telegram_message(mesaj)
    else:
        mesaj = f"{yeni_ucret} TL {yeni_urun_adi} henüz düşmedi"
        send_telegram_message(mesaj)


import time
import schedule

schedule.every().day.at("14:00").do(urun_kontrol)  

print("Fiyat kontrol sistemi çalışıyor...")
