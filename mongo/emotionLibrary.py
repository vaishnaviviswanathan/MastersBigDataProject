import sys
from pymongo import MongoClient
happyList = ['happy','awesome','sweet','excited','haha','funny','cool','good',
'hilarious','lit','giddy','fantastic','cure','radiance','treatment','safe',
'wellbeing','upbeat','success','cheer','dear','impressive','recover','wonder',
'marry','bright','win','victory','champion]','positive','better','enjoy',':D',
':)','glad','ecstatic','delighted','joy','lively','blessed','merry','peppy',
'perky','gay','jolly','chipper','bliss']
sadList = ['sad','cry','lost','death','hurt','pain','mess','miss','upset',
'cancer','disease','illness','failed','spasm','loss','grieve','sorry','weep',
'broke','mourn','divorce','tear','negative','dead',':(','bitter','despair',
'heartbroken','blue','gloomy','low','morbid','somber','reject','deject','trouble',
'alone','down','drepess','unhappy','stress','sorrow','pessimistic','weary',
'disappoint','distraught']
angryList = ['angry','hate','frustrat','mad','piss','stupid','bad','evil',
'smh','jealous','failure','retard','bitch','wreck','resist','dumb','liar',
'lie','liar','toxic','scowl','brutal','sugarcoat','break','steal','wrong',
'screw','>:(','heated','furious','irritated','offend','outrage','resent','displease',
'fuming','raging','rage','provoke','wrath','infuriat','sulk','irate','uptight',
'antagonize','temper']
loveList = ['love','kiss','hug','content','beautiful','cute','hot','gorgeous',
'fab','luv','humble','flower','rose','pink','best','xoxo','boyfriend','girlfriend',
'husband','wife','delicious','handsome','<3','affection','appreciate','devote',
'lust','respect','tender','carring','emotion','friendship','caring'
'passion','enchant','worship','praise','cherish','fond','ador','amore','infatuat',
'bae']
fearList = ['fear','scar','blood','monster','afraid','terrif','earthquake','fire',
'terror','nervous','epdiemic','panic','phobia','histerical','paranoia',
'unease','danger','wicked','dread','crash','burn','torture','demon','invade',
'bomb','suffer','disaster','distress','numb','histeria','ominous','war','nuke']

AL = ["Alabama","AL"]
AK = ["Alaska","AK"]
AZ = ["Arizona","AZ"]
AR = ["Arkansas","AR"]
CA = ["California","CA"]
CO = ["Colorado","CO"]
CT = ["Connecticut","CT"]
DE = ["Delaware", "DE"]
FL = ["Florida","FL"]
GA = ["Georgia","GA"]
HI = ["Hawaii","HI"]
ID = ["Idaho","ID"]
IL = ["Illinois","IL"]
IN = ["Indiana","IN"]
IA = ["Iowa","IA"]
KS = ["Kansas","KS"]
KY = ["Kentucky","KY"]
LA = ["Louisana","LA"]
ME = ["Maine","ME"]
MD = ["Maryland","MD"]
MA = ["Massachusetts","MA"]
MI = ["Michigan","MI"]
MN = ["Minnesota","MN"]
MS = ["Mississippi","MS"]
MO = ["Missouri","MO"]
MT = ["Montana","MT"]
NE = ["Nebraska","NE"]
NV = ["Nevada","NV"]
NH = ["NewHampshire","NH"]
NJ = ["NewJersey","NJ"]
NM = ["NewMexico","NM"]
NY = ["NewYork","NY"]
NC = ["NorthCarolina","NC"]
ND = ["NorthDakota","ND"]
OH = ["Ohio","OH"]
OK = ["Oklahoma","OK"]
OR = ["Oregon","OR"]
PA = ["Pennsylvania","PA"]
RI = ["RhodeIsland","RI"]
SC = ["SouthCarolina","SC"]
SD = ["SouthDakota","SD"]
TN = ["Tennessee","TN"]
TX = ["Texas","TX"]
UT = ["Utah","UT"]
VT = ["Vermont","VT"]
VA = ["Virginia","VA"]
WA = ["Washington","WA"]
WV = ["WestVirginia","WV"]
WI = ["Wisconsin","WI"]
WY = ["Wyoming","WY"]

def emotionCount(sentence):
    emotions = [-1,-2,-3,-4,-5]
    for word in sentence.split(' '): #For loop for counting up each word that represents an emotion
        if any(x in word for x in happyList):
            if emotions[0] == -1:
                emotions[0]=0
            emotions[0] += 1
        if any(x in word for x in sadList):
            if emotions[1] == -2:
                emotions[1]=0
            emotions[1] += 1
        if any(x in word for x in angryList):
            if emotions[2] == -3:
                emotions[2]=0
            emotions[2] += 1
        if any(x in word for x in loveList):
            if emotions[3] == -4:
                emotions[3]=0
            emotions[3] += 1
        if any(x in word for x in fearList):
            if emotions[4] == -5:
                emotions[4]=0
            emotions[4] += 1

    #Emotions for the array [happy,sad,angry,love,fear]
    output = max(emotions)
    checkValid = set(emotions)
    if len(checkValid) != 5 or output == -1:
        return 0
    else:
        outputIndex = emotions.index(output)
        if outputIndex == 0:
            return 'happy'
        if outputIndex == 1:
            return 'sad'
        if outputIndex == 2:
            return 'angry'
        if outputIndex == 3:
            return 'love'
        if outputIndex == 4:
            return 'fear'

def insertDoc(date):
    client = MongoClient()
    db = client.Andrew

    emotColl = db.emotions

    emotColl.insert([
        {"date": date,"state":"AL","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"AK","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"AZ","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"AR","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"CA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"CO","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)}
        ,"num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"CT","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)}
        ,"num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"DE","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"FL","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"GA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"HI","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"ID","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"IL","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"IN","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"IA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"KS","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"KY","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"LA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"ME","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MD","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MI","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MN","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MS","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MO","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"MT","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NE","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NV","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NH","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NJ","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NM","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NY","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"NC","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"ND","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"OH","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"OK","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"OR","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"PA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"RI","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"SC","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"SD","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"TN","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"TX","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"UT","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"VT","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"VA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"WA","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"WV","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"WI","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}},
        {"date": date,"state":"WY","happy":int(0),"sad":int(0),"angry":int(0),"love":int(0),"fear":int(0),
        "num1Tweet":{"text":"","likes":int(0)},"num2Tweet":{"text":"","likes":int(0)},"num3Tweet":{"text":"","likes":int(0)},"num4Tweet":{"text":"","likes":int(0)},
        "num5Tweet":{"text":"","likes":int(0)}}
    ])

def updateLikes(date,state,text, likes):
    client = MongoClient()
    db = client.Andrew
    num1Likes = db.emotions.distinct("num1Tweet.likes",{'$and':[{"date":date},{"state":state}]})
    num2Likes = db.emotions.distinct("num2Tweet.likes",{'$and':[{"date":date},{"state":state}]})
    num3Likes = db.emotions.distinct("num3Tweet.likes",{'$and':[{"date":date},{"state":state}]})
    num4Likes = db.emotions.distinct("num4Tweet.likes",{'$and':[{"date":date},{"state":state}]})
    num5Likes = db.emotions.distinct("num5Tweet.likes",{'$and':[{"date":date},{"state":state}]})

    emotColl = db.emotions
    insert = False
    if likes > num5Likes[0]:
        if likes > num1Likes[0] and insert == False:
            temp1 = db.emotions.distinct("num1Tweet",{'$and':[{"date":date},{"state":state}]})
            temp2 = db.emotions.distinct("num2Tweet",{'$and':[{"date":date},{"state":state}]})
            temp3 = db.emotions.distinct("num3Tweet",{'$and':[{"date":date},{"state":state}]})
            temp4 = db.emotions.distinct("num4Tweet",{'$and':[{"date":date},{"state":state}]})
            db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num1Tweet.text":text,"num1Tweet.likes":likes}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num2Tweet":temp1[0]}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num3Tweet":temp2[0]}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num4Tweet":temp3[0]}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num5Tweet":temp4[0]}})
            insert = True
        if likes > num2Likes[0] and insert == False:
            temp2 = db.emotions.distinct("num2Tweet",{'$and':[{"date":date},{"state":state}]})
            temp3 = db.emotions.distinct("num3Tweet",{'$and':[{"date":date},{"state":state}]})
            temp4 = db.emotions.distinct("num4Tweet",{'$and':[{"date":date},{"state":state}]})
            db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num2Tweet.text":text,"num2Tweet.likes":likes}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num3Tweet":temp2[0]}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num4Tweet":temp3[0]}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num5Tweet":temp4[0]}})
            insert = True
        if likes > num3Likes[0] and insert == False:
            temp3 = db.emotions.distinct("num3Tweet",{'$and':[{"date":date},{"state":state}]})
            temp4 = db.emotions.distinct("num4Tweet",{'$and':[{"date":date},{"state":state}]})
            db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num3Tweet.text":text,"num3Tweet.likes":likes}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num4Tweet":temp3[0]}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num5Tweet":temp4[0]}})
            insert = True
        if likes > num4Likes[0] and insert == False:
            temp4 = db.emotions.distinct("num4Tweet",{'$and':[{"date":date},{"state":state}]})
            db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num4Tweet.text":text,"num4Tweet.likes":likes}})
            emotColl.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num5Tweet":temp4[0]}})
            insert = True
        if likes > num5Likes[0] and insert == False:
            db.emotions.update({'$and':[{"date":date},{"state":state}]},{'$set':{"num4Tweet.text":text,"num5Tweet.likes":likes}})


def checkLocation(location):

    for word in location.split(','):
        word = word.replace(" ","")
        if any(x == word for x in AL):
            return "AL"
        if any(x == word for x in AK):
            return "AK"
        if any(x == word for x in AZ):
            return "AZ"
        if any(x == word for x in AR):
            return "AR"
        if any(x == word for x in CA):
            return "CA"
        if any(x == word for x in CO):
            return "CO"
        if any(x == word for x in CT):
            return "CT"
        if any(x == word for x in DE):
            return "DE"
        if any(x == word for x in FL):
            return "FL"
        if any(x == word for x in GA):
            return "GA"
        if any(x == word for x in HI):
            return "HI"
        if any(x == word for x in ID):
            return "ID"
        if any(x == word for x in IL):
            return "IL"
        if any(x == word for x in IN):
            return "IN"
        if any(x == word for x in IA):
            return "IA"
        if any(x == word for x in KS):
            return "KS"
        if any(x == word for x in KY):
            return "KY"
        if any(x == word for x in LA):
            return "LA"
        if any(x == word for x in ME):
            return "ME"
        if any(x == word for x in MD):
            return "MD"
        if any(x == word for x in MA):
            return "MA"
        if any(x == word for x in MI):
            return "MI"
        if any(x == word for x in MN):
            return "MN"
        if any(x == word for x in MS):
            return "MS"
        if any(x == word for x in MO):
            return "MO"
        if any(x == word for x in MT):
            return "MT"
        if any(x == word for x in NE):
            return "NE"
        if any(x == word for x in NV):
            return "NV"
        if any(x == word for x in NH):
            return "NH"
        if any(x == word for x in NJ):
            return "NJ"
        if any(x == word for x in NM):
            return "NM"
        if any(x == word for x in NY):
            return "NY"
        if any(x == word for x in NC):
            return "NC"
        if any(x == word for x in ND):
            return "ND"
        if any(x == word for x in OH):
            return "OH"
        if any(x == word for x in OK):
            return "OK"
        if any(x == word for x in OR):
            return "OR"
        if any(x == word for x in PA):
            return "PA"
        if any(x == word for x in RI):
            return "RI"
        if any(x == word for x in SC):
            return "SC"
        if any(x == word for x in SD):
            return "SD"
        if any(x == word for x in TN):
            return "TN"
        if any(x == word for x in TX):
            return "UT"
        if any(x == word for x in UT):
            return "UT"
        if any(x == word for x in VT):
            return "VT"
        if any(x == word for x in VA):
            return "VA"
        if any(x == word for x in WA):
            return "WA"
        if any(x == word for x in WV):
            return "WV"
        if any(x == word for x in WI):
            return "WI"
        if any(x == word for x in WY):
            return "WY"
    return 0
