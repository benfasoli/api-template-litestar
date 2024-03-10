FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV TZ UTC

WORKDIR /app

# Install OS dependencies.
RUN apt-get update -y \
    && apt-get install -y tini

# Install python dependencies.
COPY pyproject.toml .
RUN pip install .

COPY . .
ENTRYPOINT ["tini", "--"]
CMD [ "litestar", "--app=src.app:app", "run",  "--host=0.0.0.0", "--port=8000"]
