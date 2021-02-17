FROM python:3

WORKDIR /nesabot

ADD ./requirements.txt .
COPY ./src ./src

RUN touch /tmp/nesabot_grades.json
RUN pip3 install -r ./requirements.txt

CMD [ "/nesabot/src/main.py" ]
