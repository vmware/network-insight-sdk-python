# syntax=docker/dockerfile:1
FROM python:3.7-slim-buster
WORKDIR /code

COPY . /code/databus_client/.
RUN pip install -r /code/databus_client/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code/databus_client/"
ENTRYPOINT ["python3", "/code/databus_client/endpoint/client_endpoint.py"]