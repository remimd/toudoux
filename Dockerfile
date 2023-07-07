ARG PYTHON_VERSION="3.11.4"

# Python
FROM python:${PYTHON_VERSION}-slim

ARG WORK_DIR="/toudoux"

# Working directory
WORKDIR ${WORK_DIR}
COPY . .

# Setup system
RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get autoremove
RUN apt-get clean

RUN apt-get install curl build-essential -y

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_HOME="$HOME/.poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PORT=8000
ENV UVICORN_PORT=${PORT}

EXPOSE ${PORT}

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Setup Poetry
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry config installer.modern-installation true
RUN poetry config virtualenvs.create false
RUN poetry install --compile --no-cache --sync --without dev
RUN poetry cache clear pypi --all

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--use-colors"]