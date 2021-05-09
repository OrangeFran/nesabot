FROM python:3

COPY . /nesabot
WORKDIR /nesabot

RUN pip3 install -r ./requirements.txt

CMD [ "./nesabot.py" ]
