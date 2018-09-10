import tweepy
import random
from secrets import *
from time import sleep

botname="@csfresheradvice"
seconds=3600 # seconds to wait between tweeting
filename="advice.tsv" # file with tweets in


# advice bot, derived heavily from this 
# "how to write a bot in python" tutorial
# https://scotch.io/tutorials/build-a-tweet-bot-with-python
# and this one
# https://vivshaw.github.io/blog/build-you-a-tweetbot-1/


class advicebot:
    def __init__(self, advice ):
        self.advice_lines=self.load_tweets(advice)

        #initialize Twitter authorization with Tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)

    def load_tweets(self, corpus):
        with open(corpus) as corpus_file:
            advice_lines = corpus_file.readlines()
        return advice_lines
    
    def tweet(self):
# randomly choose a message from your corpus
        message = random.choice(self.advice_lines)
# tweet it: note if you're trying stuff out coment the self.api.update line and uncomment the print line then you can see it working without spamming twitter 
        try:
            #print(message) 
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)
        
    def automate(self, delay):
        while True:
            self.tweet()
            sleep(delay)


def main():
	bot = advicebot(filename)
	bot.automate(seconds)

if __name__ == "__main__":
    main()




