# Define la imagen base
FROM python:3.9-alpine

# Establece la variable de entorno PYTHONUNBUFFERED en 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt



WORKDIR /jarvis
COPY ./ /jarvis



COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
