# Dockerfile-frontend

# Imagem base
FROM python:3.12

# Definir o diretório de trabalho no container
RUN pip install poetry 

WORKDIR /app

# Copiar os arquivos de dependências e instalar
COPY /backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app

# Comando para executar a aplicação
CMD ["poetry","run", "fastapi", "dev", "backend/main.py", "--host", "0.0.0.0", "--port", "8000"]