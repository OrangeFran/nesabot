# Nesabot

Receive notifications when new grades get upload to the NESA portal.
Free and easy to use and deploy.

## Setup 

First of all, go to [IFTTT](https://ifttt.com) and create a new applet.
For the _if_, choose `webhook` and for the _then that_, choose `notification`.

After that, copy the webhook url and run the following command in your terminal:
```
cp .env.template .env.local
```

Then open the new file and fill in you webhook url, your username and your password.
Now you are ready to deploy the code. Follow the steps below to continue. You can choose between the
[Heroku](https://heroku.com) free tier and your own docker daemon if you have one.

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
It will store them as json for future reference. If new grades were uploaded, it will notify
you over [IFTTT](https://ifttt.com).
