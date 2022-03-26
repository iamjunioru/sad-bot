# sad bot
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
    p1 = ['Se meus olhos mostrassem a minha alma, todos, ao me verem sorrir, chorariam comigo.',
          'Feliz na tristeza, triste na alegria.',
          'A falta de amigos faz com que o mundo pareça um deserto.',
          'Eu não sinto mais nada.',
          'A vida é apenas uma visão momentânea das maravilhas deste assombroso universo, e é triste que tantos se desgastem sonhando com fantasias espirituais.',
          'Mantenha um pouco de coragem no seu coração e use para viver amanhã.',
          'Gosto de fazer as pessoas felizes, mesmo quando eu estou triste.',
          ':(',
          'Eu não sei mais qual é o meu estado emocional, sério. Não sei se estou feliz ou triste. Apenas sinto um vazio dentro de mim.',
          "Um amigo de verdade consegue enxergar a tristeza em seus olhos, quando todas as outras pessoas apenas enxergam o seu sorriso.",
          "Ontem depois que você foi embora confesso que fiquei triste como sempre. Mas, pela primeira vez, triste por você.",
          "Ando tão triste, sem direção.",
          "Eu sei que tudo isso serão apenas histórias algum dia. E nossas fotos se tornarão velhas fotografias. E todos nós nos tornaremos mãe ou pai de alguém. Mas agora, exatamente agora, esses momentos não são histórias. Está acontecendo. Eu posso ver. E nesse momento, somos o infinito.",
          "Se num dia de tristezas, tiveres de escolher entre o mundo e o amor... Escolhe o amor e com ele conquista o mundo!",
          "As pessoas mais solitárias são as mais amáveis. As mais tristes têm o sorriso mais bonito. As mais sofridas são as mais sábias. Tudo porque elas não desejam que outras pessoas sofram o tanto quanto elas sofreram.",
          "Essa dor também é o que te dá força.",
          "É triste quando você percebe que não é tão importante para alguém como você pensou que era.",
          "O mais triste de um passarinho engaiolado é que ele se sente bem.",
          "O amor é a coisa mais alegre. O amor é a coisa mais triste. O amor é a coisa que eu mais quero.",
          "É triste esquecer um amigo. Nem todo mundo tem amigo.",
          "Por você, eu seria capaz de fingir estar feliz mesmo estando triste. Por você, eu seria capaz de fingir ser forte mesmo estando machucado.",
          "A tristeza também provoca doenças.",
          "Triste mesmo é a gente nem saber que o fim ainda nem começou e que perdemos a pessoa amada logo no começo.",
          "Sobre as asas do tempo, a tristeza vai-se embora.",
          "Quando fizeres algo nobre e belo e ninguém notar, não fique triste. Pois o sol toda manhã faz um lindo espetáculo e no entanto, a maioria da plateia ainda dorme...",
          "A tristeza vai durar para sempre. - Vincent Van Gogh",
          "Quando você compara as tristezas da vida real com os prazeres da imaginária, você não vai querer viver de novo, somente sonhar para sempre.",
          "Irônico: Lembranças felizes nos fazem chorar de tristeza.",
          "As palavras salvaram-me sempre da tristeza.",
          "É triste saber que falta alguma coisa e saber que não dá pra comprar, substituir, esquecer, implorar.",
          "Ando tão só. Ando tão triste que às vezes me jogo na cama, meto a cara fundo no travesseiro e quase começo a chorar. Sempre lembro de você nessas horas.",
          "Quando estiver triste, apenas feche os olhos e pense naquilo que te faz sorrir."]
  
    final_phrase = random.choice(p1)
    return final_phrase

while True:
    api.update_status(status=random_phrase().lower())
    print('------------------------------------------')
    print('um tweet triste foi enviado com sucesso!')
    print('------------------------------------------')
    sleep(500) # a cada x min
