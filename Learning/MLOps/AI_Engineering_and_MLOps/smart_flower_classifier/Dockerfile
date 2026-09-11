FROM python:3.11-alpine

WORKDIR /app

# Installer gcc pour certaines bibliothèques ML
RUN apk add --no-cache gcc g++ libstdc++ bash

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]