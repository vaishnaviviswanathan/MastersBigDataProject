# Using kafka-python opensource library

#gnip
import requests
import json
from requests.auth import HTTPBasicAuth

#kafka
from kafka import KafkaProducer
from kafka.errors import KafkaError

#Connecting to GNIP API with authentication
hashtag = raw_input("Enter the hashtag keyword")
maxresults = raw_input("Enter the max tweet results")
fromDate = raw_input("Enter the max tweet results in the format YYYYMMDDHHMM ex: 201703170000")
toDate = raw_input("Enter the max tweet results in the format YYYYMMDDHHMM ex: 201703190000")

url = 'https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json?query=%23'+hashtag+'&maxResults='+maxresults+'&fromDate=201703170000&toDate=201703190000'
r = requests.get(url, auth=HTTPBasicAuth('zachary.l.johnson@colorado.edu', 'n3th3rlandstorm8'))

producer = KafkaProducer(bootstrap_servers=['172.31.43.251:9092'])

# Asynchronous by default
producer.send('twitter1', r.content)
