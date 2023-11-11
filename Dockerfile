FROM python:3.11

WORKDIR /code

COPY ./.env /code/.env
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock

RUN pip install --upgrade pip && pip install poetry
RUN poetry install

COPY ./t_backend /code/t_backend
CMD ["poetry", "run", "uvicorn", "t_backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
