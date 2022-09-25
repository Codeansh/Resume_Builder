FROM python:3.10.7-slim-buster

WORKDIR /cv_app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wkhtmltopdf



COPY . ./

EXPOSE 8000:8000

CMD "python3" "manage.py" "runserver" "0.0.0.0:8000"