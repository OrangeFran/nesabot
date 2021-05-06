# Nesabot

Check your grades directly from telegram.
Easy to use and deploy.

## Usage

Create the `src/creds.py` file and enter the following information:

``` python
UNAME = ""                  # str
PASSWD = ""                 # str

TOKEN = ""                  # str
MY_CHAT_ID = 1              # int
```

## Heroku free tier

With the heroku free tier you can run this bot for free.
Open an account, download the cli, login and deploy the `worker`.

```
heroku container:login
heroku container:push -a nesabot worker
heroku ps:scale -a nesabot worker=1
```

## With your own docker instance

Just build the docker image and deploy it.
This would look something like this:

``` bash
docker build -t orangefran/nesabot -f Dockerfile .
docker run -d orangefran/nesabot
```

## How it works

The bot will log into your nesa account every 10 minutes and check your grades.
It will store them as json for future reference. If new grades were uploaded, the bot will notify
you and you can directly check them from telegram.
