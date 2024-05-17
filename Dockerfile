FROM python:3.12-bullseye

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]