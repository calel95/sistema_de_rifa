#Fockerfile-backend

#imagem
FROM python:3.12

#diretorio de trabalho do container
WORKDIR /app

#Copia arquivos de dependencias e instala
COPY  requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#copia o restante dos arquivos do projeto
COPY . /app

#comando para executar a aplicacao
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]