# Dockerfile-frontend

# Imagem base
FROM python:3.12

# Definir o diretório de trabalho no container
RUN pip install poetry 


WORKDIR /app

# Copiar os arquivos de dependências e instalar
COPY /frontend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app

# Comando para executar a aplicação
CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]