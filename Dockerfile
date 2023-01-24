FROM python:3.6-slim

EXPOSE 5000

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "flask_api.py"]