import requests
import json
from requests.auth import HTTPBasicAuth

#New York City
#parameters = {"lat": 40.71, "lon": -74}
#url = 'https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json'
#r = requests.get(url, data={'query':'gnip','maxResults':10}, auth=HTTPBasicAuth('zachary.l.johnson@colorado.edu', 'n3th3rlandstorm8'))
#print r.content

def save_file(r):
	with open('tweets.json', 'w') as outfile:
    	 json.dump(r.content, outfile)


#Connecting to GNIP API with authentication
hashtag = raw_input("Enter the hashtag keyword")
maxresults = raw_input("Enter the max tweet results")
fromDate = raw_input("Enter the max tweet results in the format YYYYMMDDHHMM ex: 201703170000")
toDate = raw_input("Enter the max tweet results in the format YYYYMMDDHHMM ex: 201703190000")

url = 'https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?query=%23'+hashtag+'&maxResults='+maxresults+'&fromDate=201703170000&toDate=201703190000'
r = requests.get(url, auth=HTTPBasicAuth('zachary.l.johnson@colorado.edu', ''))
print r.content

#Saving the contents to file
save_file(r)
