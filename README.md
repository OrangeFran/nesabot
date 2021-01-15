# Nesabot

Check your grades directly from telegram.
Easy to deploy and easy to use.

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
docker build -t nesabot -f dockerfile .
docker run nesabot 
```

The scripts are just for debugging.

## How it works

The bot will log into your nesa account every five minutes and check your grades.
For future reference, it will store them as json. If a new grades was uploaded, the bot will notify
you and you can directly check the grade from telegram.

Important commands (in the telegram chat):

```
/grades # Get the stored grades
/fetch  # Manually get grades from the website
/help   # A help menu
```

I hope it helps you as much as it does me.
