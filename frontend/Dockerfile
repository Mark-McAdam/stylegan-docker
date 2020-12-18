# frontend/Dockerfile

FROM python:3.8-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install \
    'git' -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]