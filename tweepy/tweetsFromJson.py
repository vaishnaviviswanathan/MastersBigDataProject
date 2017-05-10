import json


with open('happy.json', 'r') as f:
    for line in f:
            tweetObj = json.loads(line) # load it as Python dict
            #print(json.dumps(tweet['text'], indent=4)) # pretty-print
            keys =  tweetObj.keys()
            #print keys
            if 'text' in tweetObj:
                #print tweetObj['created_at'],tweetObj['text'],(tweetObj.get('user', {}).get('location', {})),(tweetObj.get('user', {}).get('favourites_count', {})),'\n'
                #print tweetObj['coordinates']
                #print tweetObj['user']['favorites_count']
                #print(tweetObj.get('user', {}).get('location', {}))
                #print(tweetObj.get('favorited_status', {}).get('favorite_count', {}))
                #print tweetObj['favorite_count']
                s = tweetObj['created_at']
                data = s.split(' ')
                date = data[1]+' '+data[2]+' '+data[5]
                print date,tweetObj['text'],(tweetObj.get('user', {}).get('location', {})),(tweetObj.get('user', {}).get('favourites_count', {})),'\n'
                #print tweetObj.get('user', {}).get('location', {})
            else:
                print 'This does not have a text entry' 