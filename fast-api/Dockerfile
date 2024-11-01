FROM python:3.11-buster


RUN pip install --upgrade pip
RUN pip install poetry

COPY ./ /app/

WORKDIR   /app

RUN poetry install

EXPOSE 8080
CMD poetry run python app.py

