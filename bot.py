import tweepy
import schedule
import time
from datetime import datetime, timedelta

api_key = ''
api_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

def countdown_to_thursday():
    today = datetime.now()
    thursday = today + timedelta(days=(3 - today.weekday() + 7) % 7, hours=14, minutes=1)
    time_until_thursday = thursday - today
    days, seconds = time_until_thursday.days, time_until_thursday.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    tweet_message = f"Faltan {days} días, para que salga nuevo episodio de Jujutsu Kaisen.\nPágina de JJK en Crunchyroll: https://www.crunchyroll.com/es/series/GRDV0019R/jujutsu-kaisen\n\n#JujutsuKaisen #JJK #JujutsuKaisenSeason2 🔔"
    client.create_tweet(text = tweet_message)
    print(f"Tweet enviado - {tweet_message}")

def on_thursday():
    tweet_message_hoy = f"¡Es hoy, es hoy! Ya está disponible el nuevo episodio de Jujutsu Kaisen.\nPágina de JJK en Crunchyroll: https://www.crunchyroll.com/es/series/GRDV0019R/jujutsu-kaisen\n\n#JujutsuKaisen #JJK #JujutsuKaisenSeason2 🔔"
    client.create_tweet(text = tweet_message_hoy)
    print(f"Tweet enviado - {tweet_message_hoy}")

# Programar el tweet diario a las 14:01
schedule.every().day.at("16:01").do(countdown_to_thursday)

# Programar el tweet especial los jueves a las 14:01
schedule.every().thursday.at("16:01").do(on_thursday)

# Mantener el script en ejecución
while True:
    schedule.run_pending()
    time.sleep(1)
