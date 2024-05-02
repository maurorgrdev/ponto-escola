# Use a imagem base do Python
FROM python:3.12.2

# Define a variável de ambiente para evitar problemas com buffers de stdout/stderr
ENV PYTHONUNBUFFERED 1

# Atualize o gerenciador de pacotes do sistema
RUN apt-get update

# Instale as dependências do sistema
RUN apt-get update

# Crie e defina o diretório de trabalho
WORKDIR /backend

# Copie o arquivo de requisitos e instale as dependências do Python
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do aplicativo para o contêiner
COPY . /backend/


# Execute o aplicativo Flask
CMD ["python", "run.py"]
