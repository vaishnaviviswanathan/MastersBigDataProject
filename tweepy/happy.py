import tweepy
import os
import time

from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
            try:
                with open('happy.json', 'a') as f:
                    f.write(data)
                    return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True
 
    def on_error(self, status):
        print(status)
        return True

 
#import configparser
#settings = configparser.ConfigParser()
#settings._interpolation = configparser.ExtendedInterpolation()
#settings.read("/Users/vaishnaviviswanathan/Documents/SEMESTER4/python/config.ini")
#settings.sections()
#CONSUMER_KEY = settings.get('Credentials', 'CONSUMER_KEY')
#CONSUMER_SECRET = settings.get('Credentials', 'CONSUMER_SECRET')
#ACCESS_TOKEN = settings.get('Credentials', 'ACCESS_TOKEN')
#ACCESS_TOKEN_SECRET = settings.get('Credentials', 'ACCESS_TOKEN_SECRET')


if(os.environ.get('CONSUMER_KEY')):
	CONSUMER_KEY=os.environ.get('CONSUMER_KEY')
else:
	print "Set CONSUMER_KEY as one of your environmental variables"

if(os.environ.get('CONSUMER_SECRET')):
	CONSUMER_SECRET=os.environ.get('CONSUMER_SECRET')
else:
	print "Set CONSUMER_SECRET as one of your environmental variables" 


if(os.environ.get('ACCESS_TOKEN')):
	ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
else:
	print "Set ACCESS_TOKEN as one of your environmental variables"	

if(os.environ.get('ACCESS_TOKEN_SECRET')):
	ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')
else:
	print "Set ACCESS_TOKEN_SECRET as one of your environmental variables"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#status = "Posting a feed using python and tweepy! - With hidden login credentials - Final!"
#api.update_status(status=status)

#start_time = time.time() #grabs the system time
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#happy','#awesome','#sweet','#excited','#lol','#haha','#funny','#cool','#good','#hilarious'])



