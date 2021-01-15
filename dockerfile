FROM python:3

RUN mkdir -p /nesabot
WORKDIR /nesabot

ADD ./requirements.txt .

RUN mkdir cache && touch cache/grades.json 
COPY ./src src

RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements.txt

CMD ["/nesabot/venv/bin/python3", "/nesabot/src/main.py"]
