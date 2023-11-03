FROM ubuntu

RUN apt update && apt upgrade -y
RUN apt install python

WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./config.json ./config.json

ENV PYTHONPATH=/usr/app/src

CMD [ "python", "src/main.py" ]