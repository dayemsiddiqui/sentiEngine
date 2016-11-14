import tweepy



class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

class tweetMonitoringService:

    def __init__(self):
        consumer_key = "kM6QNIld41CCYJisPTECdN6Yp"
        consumer_secret = "DtPBjdvPi7b4qCOjQqRIpKNeQLOAPDS1DIuS0RCs0jlE6fMkG6"
        access_token = "3382848435-mePu89dSShZFXgD74KZNpGXZ9I2c5HBE7LkhfYR"
        access_token_secret = "5RErKexnXm83lzUoakX9d4XLurhgUqeZHxufTzZfcLRtu"
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def getApi(self):
        return self.api

    def startTracking(self):
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = self.api.auth, listener=myStreamListener)
        myStream.filter(track=['python'], async=True)





tweetmon = tweetMonitoringService()
tweetmon.startTracking()
