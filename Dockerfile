# Dockerfile-frontend

# Imagem base
FROM python:3.12

# Definir o diretório de trabalho no container
RUN pip install poetry

COPY . /frontend

WORKDIR /frontend

# Copiar os arquivos de dependências e instalar

RUN poetry install

# Copiar o restante dos arquivos do projeto
COPY . /app

EXPOSE 8501

# Comando para executar a aplicação
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]