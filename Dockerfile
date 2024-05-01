# Use a imagem base do Python
FROM python:3.12.2

# Define a variável de ambiente para evitar problemas com buffers de stdout/stderr
ENV PYTHONUNBUFFERED 1

# Atualize o gerenciador de pacotes do sistema
RUN apt-get update

# Instale as dependências do sistema
RUN apt-get install -y nginx

# Crie e defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY docker-entrypoint.sh /app/docker-entrypoint.sh

# Copie o código do aplicativo para o contêiner
COPY . /app/


# Execute o aplicativo Flask
CMD ["python", "run.py"]
