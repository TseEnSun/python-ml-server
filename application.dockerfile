FROM python:3.10

WORKDIR /

ENV PYTHONPATH=/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /

RUN poetry install --only main

COPY ./ /
RUN chmod +x /app/start-uvicorn.sh

CMD bash /app/start-uvicorn.sh
