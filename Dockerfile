# Use a imagem base Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie todo o código fonte para o contêiner
COPY . .

# Comando para executar a aplicação quando o contêiner for iniciado
CMD [ "python", "./main.py" ]
