# Nesabot

Check your grades directly from telegram.
Tested with the website from the `Kantonsschule am Burggraben`: `https://ksbg.nesa-sg.ch`.
Easy to use and deploy.

## Usage

Create the `src/creds.py` file and enter the following information:

``` python
UNAME = ""                  # str
PASSWD = ""                 # str

TOKEN = ""                  # str
MY_CHAT_ID = 1              # int
```

Just build the docker image and deploy it.
This would look something like this:

``` bash
docker build -t nesabot -f Dockerfile .
docker run nesabot 
```

The scripts are just for debugging.

To transfer the docker image to your server, you can save the file and copy it over the internet:
``` bash
docker save -o nesabot.tar.gz nesabot
docker -H ssh://your@server load -i nesabot.tar.gz
```

## How it works

The bot will log into your nesa account every five minutes and check your grades.
It will store them as json for future reference. If new grades were uploaded, the bot will notify
you and you can directly check them from telegram.

Important commands (in the telegram chat):

``` bash
/grades # Get the stored grades
/fetch  # Manually get grades from the website
/help   # A help menu
```

I hope it helps you as much as it does me.
