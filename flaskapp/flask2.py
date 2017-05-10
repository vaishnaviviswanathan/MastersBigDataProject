import sys
import pymongo

from pymongo import MongoClient
from flask import Flask, render_template, jsonify
app = Flask(__name__)

client = MongoClient("mongodb://FILL/FILL")
db = client.EmotionalState
#db = client.Andrew

states = [0] * 50
listStates = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN",
"IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC",
"ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

@app.route("/")
def hello():
	i=0

	for x in listStates:
		emotion = [0,0,0,0,0]
		happy = db.emotions.distinct("happy",{'$and':[{"state":listStates[i]},{"date":"Apr 24 2017"}]})
		sad = db.emotions.distinct("sad",{'$and':[{"state":listStates[i]},{"date":"Apr 24 2017"}]})
		love = db.emotions.distinct("love",{'$and':[{"state":listStates[i]},{"date":"Apr 24 2017"}]})
		fear = db.emotions.distinct("fear",{'$and':[{"state":listStates[i]},{"date":"Apr 24 2017"}]})
		anger = db.emotions.distinct("angry",{'$and':[{"state":listStates[i]},{"date":"Apr 24 2017"}]})
		emotion = [happy[0],sad[0],love[0],fear[0],anger[0]]

		output = max(emotion)
		outputIndex = emotion.index(output)

		if outputIndex == 0:
			states[i] = 'happy'
		if outputIndex == 1:
			states[i] ='sad'
		if outputIndex == 2:
			states[i] ='love'
		if outputIndex == 3:
			states[i] ='fear'
		if outputIndex == 4:
			states[i] ='anger'

		i+=1

	data = jsonify(AL=states[0],AK=states[1],AZ=states[2],AR=states[3],CA=states[4],CO=states[5],CT=states[6],
		DE=states[7],FL=states[8],GA=states[9],HI=states[10],ID=states[11],IL=states[12],IN=states[13],IA=states[14],
		KS=states[15],KY=states[16],LA=states[17],ME=states[18],MD=states[19],MA=states[20],MI=states[21],MN=states[22],
		MS=states[23],MO=states[24],MT=states[25],NE=states[26],NV=states[27],NH=states[28],NJ=states[29],NM=states[30],
		NY=states[31],NC=states[32],ND=states[33],OH=states[34],OK=states[35],OR=states[36],PA=states[37],RI=states[38],
		SC=states[39],SD=states[40],TN=states[41],TX=states[42],UT=states[43],VT=states[44],VA=states[45],WA=states[46],
		WI=states[47],WV=states[48],WY=states[49])

	return render_template('/../front_end/index.html', geocode=geocode)
if __name__ == "__main__":
	app.debug = True
	app.run()