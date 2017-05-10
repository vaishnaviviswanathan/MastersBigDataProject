#For Bolt
import os
from collections import Counter
from streamparse import Bolt
import json
import time

#For MongoDB
import sys
import emotionLibrary
from pymongo import MongoClient

#Bolt
class WordCountBolt(Bolt):
    outputs = ['json_object']

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        right_text = str(tup.values[0]).partition(", u'")[2]
        left_text = right_text.partition("\\r\\n'")[0]

        key1 = '"text":'
        key2 = '"source":'

        beginning = left_text.find(key1)
        end = left_text.find(key2)

        text_str = left_text[beginning:end]

        key3 = '"location":'
        key4 = '"url":'

        beginning1 = left_text.find(key3)
        beginning1 = beginning1 + 12
        end1 = left_text.find(key4)
        end1 = end1 - 2
        location_str = left_text[beginning1:end1]

        key5 = '"favourites_count":'
        key6 = '"statuses_count":'

        beginning2 = left_text.find(key5)
        beginning2 = beginning2 + 19
        end2 = left_text.find(key6)
        end2 = end2 - 2
        fav_str = left_text[beginning2:end2]
        if fav_str == '':
            fav_str = "0"

        created_str = left_text[19:22]+' '+left_text[23:25]+' '+left_text[41:45]

        self.logger.info([text_str])
        self.logger.info([created_str])
        self.logger.info([location_str])
        self.logger.info([fav_str])
        self.emit(tup.values[0])


#Mongo Code 
        valid = True
        output = emotionLibrary.emotionCount(text_str.lower())
        state = emotionLibrary.checkLocation(location_str)

        if output == 0 or state == 0:
            valid = False
            self.logger.info(["inside false"])

        if valid == True:

            client = MongoClient("mongodb://13.58.97.93/EmotionalState")
            db = client.EmotionalState #Connects to the database test
            emo = db.emotions #Making database collection for emotions to be stored

            likes = int(fav_str)
            self.logger.info([likes])
            self.logger.info(["inside true 1"])

            if db.emotions.find({"date": created_str}).count() > 0:
            #Update emotion count for the state and update 
                emotionLibrary.updateLikes(created_str,state,text_str,likes)
                db.emotions.update(
                    {'$and':[{"date":created_str},{"state":state}]},
                    {'$inc':{output:int(1)}},
                    )
                self.logger.info(["inside true if"])
            else:
            #If documents for a specific date do not exist, insert and increment
                emotionLibrary.insertDoc(created_str)
                db.emotions.update({'$and':[{"date":created_str},{"state":state}]},{'$inc':{output:int(1)}})
                db.emotions.update({'$and':[{"date":created_str},{"state":state}]},{'$set':{"num1Tweet.text":text_str,"num1Tweet.likes":likes}})
                self.logger.info(["inside true else"])
#                self.logger.info([text_str])
#                self.logger.info([created_str])
#                self.logger.info([location_str])
#                self.logger.info([fav_str])

        
if __name__ == '__main__':
        WordCountBolt().run()
