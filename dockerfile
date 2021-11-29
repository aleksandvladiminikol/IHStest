FROM python:3.9-slim as compile-image

COPY requirements.txt /requirements.txt
RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install --no-cache-dir -r /requirements.txt

ENV PYTHONPATH=${PYTHONPATH}:/app

RUN adduser docker
USER docker

WORKDIR /app
COPY ./ /app/IHStest

EXPOSE 8000
ENTRYPOINT ["/opt/venv/bin/python", "/app/IHStest/api.py"]
