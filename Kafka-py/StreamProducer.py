#stream
import tweepy
import os
import time

from tweepy import Stream
from tweepy.streaming import StreamListener

#kafka lib
from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import SimpleProducer, KafkaClient

# Kafka settings
topic = b'twitter1'
# setting up Kafka producer
kafka = KafkaClient('172.31.41.187:9092')
producer = SimpleProducer(kafka)

class MyListener(StreamListener):

    def on_data(self, data):
            try:
                producer.send_messages(topic, data.encode('utf-8'))
                return True

            except BaseException as e:
                print("Error on_data: %s" % str(e))
                return True

    def on_error(self, status):
        print(status)
        return True


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

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['happy','awesome','sweet','excited','haha','funny','cool','good','hilarious','lit','giddy','fantastic','cure','radiance','treatment','safe','wellbeing','upbeat','success','cheer','dear','impressive','recover','wonder','marry','bright','win','victory','champion','positive','better','enjoy',':D',':)','glad','ecstatic','delighted','joy','lively','blessed','merry','peppy','perky','gay','jolly','chipper','bliss','sad','cry','lost','death','hurt','pain','mess','miss','upset','cancer','disease','illness','failed','spasm','loss','grieve','sorry','weep','broke','mourn','divorce','tear','negative','dead',':(','bitter','despair','heartbroken','blue','gloomy','low','morbid','somber','reject','deject','trouble','alone','down','drepess','unhappy','stress','sorrow','pessimistic','weary','disappoint','distraught','angry','hate','frustrat','mad','piss','stupid','bad','evil','smh','jealous','failure','retard','bitch','wreck','resist','dumb','liar','lie','liar','toxic','scowl','brutal','sugarcoat','break','steal','wrong','screw','>:(','heated','furious','irritated','offend','outrage','resent','displease','fuming','raging','rage','provoke','wrath','infuriat','sulk','irate','uptight','antagonize','temper','love','kiss','hug','content','beautiful','cute','hot','gorgeous','fab','luv','humble','flower','rose','pink','best','xoxo','boyfriend','girlfriend','husband','wife','delicious','handsome','<3','affection','appreciate','devote','lust','respect','tender','carring','emotion','friendship','caring','passion','enchant','worship','praise','cherish','fond','ador','amore','infatuat','bae','fear','scar','blood','monster','afraid','terrif','earthquake','fire','terror','nervous','epdiemic','panic','phobia','histerical','paranoia','unease','danger','wicked','dread','crash','burn','torture','demon','invade','bomb','suffer','disaster','distress','numb','histeria','ominous','war','nuke'])
