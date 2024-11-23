ARG GATEWAY

FROM python:3.10-slim

WORKDIR /api

COPY requirements.txt .

COPY ./$GATEWAY/ .

RUN pip install -r requirements.txt

CMD [ "python", "api/api.py" ]
