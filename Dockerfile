FROM python:3.13.3

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "gunicorn", "main:app"]