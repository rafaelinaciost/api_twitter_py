# NO TERMINAL (VSCODE)
# instalando o virtualenv no vscode ( pip install virtualenv )
# criando o ambiente  virtual ( virtualenv venv )
# ativando o ambiente virtual no windows ( venv\Scripts\activate )
# dentro do ambiente virtual instale a biblioteca tweepy ( pip install tweepy )

# criar um aplicativo no twitter para obter as credenciais de acesso necessárias ( chaves api e tokens de acesso)

import tweepy  
import matplotlib.pyplot as plt

consumer_key = 'sua_consumer_key'
consumer_secret = 'sua_consumer_secret'
access_token = 'seu_access_token'
access_token_secret = 'seu_access_token_secret'

#autenticação com api do twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# interagir com a API do twitter
tweets = api.search_tweets(q='python' , count=10)
for tweet in tweets:
    print(tweet.text)


# Pesquisa por Tweets de um Determinado Usuário:
def get_user_tweets(username, count=10):
    user_tweets = api.user_timeline(screen_name=username, count=count)
    for tweet in user_tweets:
        print(tweet.text)   


# Pesquisa por Tweets em uma Localização Geográfica Específica:
geocode = "-22.9035,-43.2096,100km"  # Latitude, Longitude, Raio
location_tweets = api.search_tweets(q='palavra_chave', geocode=geocode, count=10)
for tweet in location_tweets:
    print(tweet.text)


#Pesquisa por Tweets em um Determinado Intervalo de Datas:
since_date = "2023-01-01"
until_date = "2023-01-31"
date_tweets = api.search_tweets(q='palavra_chave', since=since_date, until=until_date, count=10)
for tweet in date_tweets:
    print(tweet.text)



#Geração de Relatórios

# Função para gerar relatório com base nos dados coletados
def generate_report(data):
    # Processamento dos dados e geração de visualizações
    # Exemplo de criação de um gráfico de barras para contar o número de tweets por usuário
    users = [tweet.user.screen_name for tweet in data]
    user_counts = {user: users.count(user) for user in set(users)}
    
    plt.bar(user_counts.keys(), user_counts.values())
    plt.xlabel('Usuários')
    plt.ylabel('Número de Tweets')
    plt.title('Número de Tweets por Usuário')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Exemplo de uso da função para gerar relatório
if __name__ == "__main__":
    # Suponha que 'data' seja uma lista de tweets coletados
    data = [...]  # Seus dados coletados aqui
    generate_report(data)

# Certifique-se de substituir 'sua_consumer_key', 'sua_consumer_secret', 'seu_access_token', 'seu_access_token_secret', 'nome_do_usuario', 'palavra_chave', 'Latitude', 'Longitude', 'Raio', '2023-01-01' e '2023-01-31' pelos valores adequados para sua consulta específica.



