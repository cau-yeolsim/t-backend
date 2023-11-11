FROM python:3.11

WORKDIR /code

COPY ./env /code/env
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock

RUN poetry install

COPY ./t_backend /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]