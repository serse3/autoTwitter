#Api key: ywyibwUnKHOHshdzU3tvGMFDy
#Api secret key: xagFFxDQukq1kKq7MJkD2EhQjPBxWdhJazlIPqwwgIIeTT0bCz
#Bearer token: AAAAAAAAAAAAAAAAAAAAAJhYsQEAAAAA93G0AoPjlVox1GgmhaYV7Qu%2FOTM%3DXc16hnWAt1Y4CwRId7zPHNu86szegoAa98Jbng9nHNjjDCYxnv
#Acces token: 975906472793198592-BCy9hpxJR0V8sxAR99LOMrSQxR49vze
#Access token secret: 4BYFBqopLazApPL9Xoz1LIr9VZ3K9XyQnUJecmGT80lmD

import tweepy
import streamlit as st

# Crea un título
st.title("Hello, this is autotwitter")

# Configura las claves de API de Twitter
consumer_key = "ywyibwUnKHOHshdzU3tvGMFDy"
consumer_secret = "xagFFxDQukq1kKq7MJkD2EhQjPBxWdhJazlIPqwwgIIeTT0bCz"
access_token = "975906472793198592-BCy9hpxJR0V8sxAR99LOMrSQxR49vze"
access_token_secret = "4BYFBqopLazApPL9Xoz1LIr9VZ3K9XyQnUJecmGT80lmD"

# Crea una instancia de la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Crea un botón para publicar un Tweet
if st.button("Publicar Tweet"):
    # Obtiene el texto del Tweet
    tweet_text = st.text_input("Hello world")
    # Publica el Tweet
    api.update_status(tweet_text)
    # Muestra un mensaje de éxito
    st.success("¡Tweet publicado!")
