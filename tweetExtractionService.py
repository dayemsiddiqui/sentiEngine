from TwitterSearch import *
from peewee import *
import time
import threading

db = SqliteDatabase('tweets.db')





class TweetExtractor():

    def __init__(self):
        self.consumer_key = "eCw64tkhBc4X1g3iIMR4lU7LG"
        self.consumer_secret = "eJvv2arJsGEY1QjM10mcqheb1OhpJLZ86T4Sdn3lVWG7Zjnnmw"
        self.access_token = "3382848435-aSQ0cXU9zkMfQrvlGjNIqfhcBgH0ZU3OBWzF0aD"
        self.access_token_secret = "NWaiswshbFTw0GHfaNF87XYSMpxU9xaBicAX2wcRkqfhh"
        self.keywords = set()

    def addKeyword(self, word):
        self.keywords.add(word)

    def removeKeyword(self, word):
        self.keywords.remove(word)


    def startPrinting(self):
        while True:
            print self.keywords

    def startMining(self):
        try:
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.set_keywords(self.keywords) # let's define all words we would like to have a look for
            # tso.set_language('de') # we want to see German tweets only
            tso.set_include_entities(False) # and don't give us all those entity information

            # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                consumer_key = self.consumer_key,
                consumer_secret = self.consumer_secret,
                access_token = self.access_token,
                access_token_secret = self.access_token_secret
            )

            sleep_for = 60 # sleep for 60 seconds
            last_amount_of_queries = 0 # used to detect when new queries are done

             # this is where the fun actually starts :)
            for tweet in ts.search_tweets_iterable(tso):
                print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

                current_amount_of_queries = ts.get_statistics()[0]
                if not last_amount_of_queries == current_amount_of_queries:
                    last_amount_of_queries = current_amount_of_queries
                    time.sleep(sleep_for)

        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)

miner = TweetExtractor()
miner.addKeyword("dawlance")
miningThread = threading.Thread(target=miner.startPrinting)
miningThread.start()
time.sleep(60)
miner.addKeyword("IBA")
