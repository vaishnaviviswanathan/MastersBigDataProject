import sys
from pymongo import MongoClient

client = MongoClient()

db = client.Andrew #Connects to the database test
emo = db.emotions #Making database collection for emotions to be stored

state = "CO"
date = "4/11/2017"
happyNum = 15
sadNum = 13
angryNum = 10
loveNum = 9
fearNum = 4
# db.restaurant relates to the collection restaurant inside the database db(test).
result = db.restaurants.insert_one( #Result will be equal to the _id of what was inserted
    {
        "date":{
            date:{
                "state":{
                    state:{
                        "happy":happyNum,
                        "sad":sadNum,
                        "angry":angryNum,
                        "love":loveNum,
                        "fear":fearNum
                    }
                }
            }
        }

    }
)
