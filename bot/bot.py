from time import sleep
from httplib2 import Response
import tweepy
import random

bearer_token = ''
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token=access_token, access_token_secret=access_token_secret, callback=Response)
api = tweepy.API(auth)

def random_phrase():
    p1 = ['ontem', 'hoje', 'agora', 'nesse exato momento', 'nesse momento...' 'antes de ontem', 'agr pouco', 'algumas horas atrás', 'horas atrás']
    p2 = [' eu percebi', ' percebemos', ' eu senti', ' sentimos', ' eu alertei' ' alertamos', ' avisamos', ' ressentimos', ' apoiamos', ' discordamos', ' repudiamos', ' odiamos']
    p3 = [' a falta', ' que a tristeza' ' a carência', ' a desmoralidade', ' o abuso', ' a indecência', ' a decadência']
    p4 = [' de amor', ' de empatia', ' da genialidade', ' de ideologia', '', ' da humanidade', ' de respeito', ' da malandragem']
    p5 = ['', ' por parte', ' a partir', '', '']
    p6 = [' do naruto', ' do bolsonaro', ' da dilma', ' do junior que me criou', ' do luffy', ' do jimin', ' do tanjiro', ' do lula', ' do anime jojo', ' do freefire', ' da fortnite', ' do league of legends']
    # p7 = [' #', ' #', ' #', ' #', '']
    
    final_phrase = random.choice(p1) + random.choice(p2) + random.choice(p3)  + random.choice(p4) + random.choice(p5) + random.choice(p6)# + random.choice(p7)
    return final_phrase

while True:
    api.update_status(status=random_phrase())
    print('o tweet foi feito com sucesso!')
    sleep(120)