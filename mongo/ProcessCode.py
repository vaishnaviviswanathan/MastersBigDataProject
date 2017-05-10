import sys
import emotionLibrary
from pymongo import MongoClient

valid = True

text = "Why are people so fantastic" #Test
output = emotionLibrary.emotionCount(text.lower())

state = emotionLibrary.checkLocation("Los Angeles, CA") #Test

if output == 0 or state == 0:
    valid = False

if valid == True:

    client = MongoClient()

    db = client.Andrew #Connects to the database test
    emo = db.emotions #Making database collection for emotions to be stored

    date = "4/12/2017" #Test
    likes = int(1200) #Test
    # db.restaurant relates to the collection restaurant inside the database db(test).

    if db.emotions.find({"date": date}).count() > 0:
        #Update emotion count for the state and update 
        emotionLibrary.updateLikes(date,state,text,likes)
        db.emotions.update(
            {'$and':[{"date":date},{"state":state}]},
            {'$inc':{output:int(1)}},
            )
    else:
        #If documents for a specific date do not exist, insert and increment
        emotionLibrary.insertDoc(date)
        db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$inc':{output:int(1)}})
        db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num1Tweet.text":text,"num1Tweet.likes":likes}})
