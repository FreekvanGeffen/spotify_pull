FROM python:3.11-slim

ENV COVERAGE_FILE=/tmp/coverage
ENV PYTHONPATH=$PYTHONPATH:.

WORKDIR /usr/src

# no version-pinning here
RUN pip install --upgrade pip \
 && pip install --no-cache-dir \
      python-dotenv \
      spotipy \
      mypy \
      ruff

COPY code_folder code_folder