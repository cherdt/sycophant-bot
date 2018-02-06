# sycophant-bot
A bot that favorites and retweets a user's most recent tweet

## Dependencies

* python
* pip
* birdy - https://github.com/inueni/birdy
* a twitter account - https://twitter.com
* a twitter app - https://apps.twitter.com

## Usage

* Copy `config.py.template` to `config.py`
* As any twitter user, create a twitter app at https://apps.twitter.com
* Enter the Consumer Key and Consumer Secret from the app in `config.py`
* Log in to twitter as the bot user (the user who will do the rewteeting and following)
* Run the auth.py script: `python auth.py`
* Enter the OAuth Key and OAuth Secret in `config.py`
* Run the stan.py script with a target user: `python stan.py cherdt`
* The first time you run stan.py for a user, it will initialize a state file but won't retweet or favorite anything.
* On subsequent runs, it will check for newest tweet from the target user and favorite and retweet it.

## Why?

This is basically a small example of how to get an access token from twitter for a 3rd-party app. That's all. It was a helpful exercise for me and maybe it will be helpful to you.

## Questions, comments, etc.

Open an issue on the GitHub site. I generally respond.