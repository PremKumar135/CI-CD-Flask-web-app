FROM python:3.11-slim

WORKDIR /app

# copy all the files
COPY src /app/src
COPY tests /app/tests
COPY .python-version .
COPY pyproject.toml .
COPY uv.lock .

# install dependencies using uv
RUN pip install uv
RUN uv venv
RUN uv pip install -r pyproject.toml
RUN uv sync

# Expose the port where the server runs on
EXPOSE 8050

# command to run the server
CMD ["uv", "run", "src/main.py"]