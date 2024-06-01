FROM python:3.11-slim

ENV COVERAGE_FILE=/tmp/coverage
ENV PYTHONPATH=$PYTHONPATH:.

WORKDIR /usr/src

# no version-pinning here
RUN pip install --upgrade pip \
 && pip install --no-cache-dir \
      spotipy \
      mypy \
      ruff

COPY spotify_pull spotify_pull