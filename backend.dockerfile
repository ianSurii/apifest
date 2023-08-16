FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app/

EXPOSE 80
ENV EXAMPLE=EXAMPLE
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./app/pyproject.toml ./app/poetry.lock* /app/
RUN chmod +x /start.sh
CMD ["/start.sh"]
