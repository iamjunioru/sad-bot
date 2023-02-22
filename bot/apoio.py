from time import sleep, time
from httplib2 import Response
import tweepy
import random

api_key = ''
api_key_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token=access_token, access_token_secret=access_token_secret, callback=Response)
api = tweepy.API(auth)

def random_phrase():
    p1 = ['Se meus olhos mostrassem a minha alma, todos, ao me verem sorrir, chorariam comigo.',
          'Feliz na tristeza, triste na alegria.',
          'A falta de amigos faz com que o mundo pareça um deserto.',
          'Eu não sinto mais nada.',
          'A vida é uma grande mentira.']
        
    final_phrase = random.choice(p1)
    return final_phrase

def random_response():
    p1 = ['tá tudo bem?',
          'como você tá se sentindo?',
          'tô aqui para conversar se você quiser.',
          'relaxa, as coisas vão melhorar.']
        
    final_phrase = random.choice(p1)
    return final_phrase

#
keyword = 'suicidio'
interval = 259200  # intervalo em segundos entre as respostas (3 dias)
last_time = time()  # tempo da última vez que o bot respondeu
count = 0  # número de pessoas que o bot respondeu desde a última vez que esperou

while True:
    try:
        if time() > last_time + interval:
            last_time = time()
            count = 0

        # procura por tweets com a palavra-chave
        tweets = tweepy.Cursor(api.search_tweets,
                               q=keyword,
                               lang="pt",
                               tweet_mode='extended').items(100)

        for tweet in tweets:
            if tweet.user.screen_name == 'sad_bot':
                continue
            # verifica se o tweet é recente o suficiente
            tweet_time = tweet.created_at.timestamp()
            if tweet_time < last_time:
                continue
            # responde ao tweet a cada 3 dias
            if count == 0:
                response = random_response()
                api.update_status('@' + tweet.user.screen_name + ' ' + response, in_reply_to_status_id=tweet.id)
                print('---------------------------------------------------------')
                print(f'o tweet de {tweet.user.screen_name} foi respondido com a frase "{response}"')
                print('---------------------------------------------------------')
                count += 1

        time_left = interval - (time() - last_time)
        print(f'esperando {time_left} segundos para buscar mais tweets...')
        sleep(time_left)

    except tweepy.TweepError as e:
        print(f'Erro ao buscar tweets: {e}')
        sleep(60)
