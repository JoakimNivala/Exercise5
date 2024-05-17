FROM python:3.12-bullseye

WORKDIR /app

COPY . /app/

COPY service_account-file.json service_account-file.json

ENV GOOGLE_APPLICATION_CREDENTIALS="service_account-file.json"

RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]