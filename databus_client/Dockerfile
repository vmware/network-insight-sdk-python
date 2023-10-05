# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster
WORKDIR /code

COPY . .
RUN pip install -r /code/network-insight-sdk-python/databus_client/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code/network-insight-sdk-python/"
ENTRYPOINT ["python3", "/code/network-insight-sdk-python/databus_client/endpoint/client_endpoint.py"]