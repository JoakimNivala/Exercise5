FROM python:3.12-bullseye

WORKDIR /app

COPY . /app/

COPY service-account-file.json /app/service-account-file.json

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/service-account-file.json"

RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]