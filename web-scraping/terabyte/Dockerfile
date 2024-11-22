FROM python:3.10

WORKDIR /api

COPY requirements.txt .

COPY ./api/ .

RUN apt update && apt install wget -y && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -fy && \
    rm google-chrome-stable_current_amd64.deb

RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
