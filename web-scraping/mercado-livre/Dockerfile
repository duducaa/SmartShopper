FROM python:3.10

WORKDIR /api

COPY requirements.txt .

COPY ./api/ .

RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
