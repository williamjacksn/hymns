FROM python:3.13-slim

RUN /usr/sbin/useradd --create-home --shell /bin/bash --user-group python

USER python
RUN /usr/local/bin/python -m venv /home/python/venv

COPY --chown=python:python requirements.txt /home/python/hymns/requirements.txt
RUN /home/python/venv/bin/pip install --no-cache-dir --requirement /home/python/hymns/requirements.txt

ENV PATH="/home/python/venv/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE="1" \
    PYTHONUNBUFFERED="1" \
    TZ="Etc/UTC"

LABEL org.opencontainers.image.source="https://github.com/williamjacksn/hymns"

COPY --chown=python:python hymns.py /home/python/hymns/hymns.py
