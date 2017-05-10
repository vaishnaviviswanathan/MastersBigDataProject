# EMOTIONAL STATE <br>

![alt tag](https://cloud.githubusercontent.com/assets/14101008/25317845/558f6f48-283e-11e7-9b46-afa88145b095.png) 
![alt tag](https://cloud.githubusercontent.com/assets/11984223/25353270/e270b14e-28eb-11e7-94cf-38a7fe6a1b3d.png) 


<br>


#### TEAM MEMBERS 

<pre>
* Andrew Callahan
* Elias Ortiz 
* Samarpita Debnath
* Vaishnavi Viswanathan
* Zachary Johnson
</pre>

#### INTRODUCTION<br>

<pre>
The objective of this project is to collect tweets from all over United States and determine the mood 
of each state and visualize these emotions in a map with accepted colors for corresponding emotions.
We collect tweets for the following emotions and visualize these emotions in a map using D3.
(Emotions are represented with the following colors)<br>
* Happy    - green
* Sad      - blue
* Anger    - red
* Love     - pink
* Fear     - black<br>
using 214 keywords
</pre>


#### TECHNOLOGIES & TOOLS <br>

<pre>
* Input API - Twitter
* Programming Language - Python, JavaScript
* Libraries used - Tweepy, pymongo, kafka-python, streamparse, lein 
* Cloud processing service - Amazon Web Service(AWS)
* Real time Processing tool - Apache Storm 
* Message - queue - Apache Kafka
* Web front end - Flask
* Database - MongoDB
* Visualization - D3
</pre>

<br>

#### TECH STACK<br>

![alt tag](https://cloud.githubusercontent.com/assets/14101008/25351299/7e24faac-28e5-11e7-9c3e-2ca008850ff7.png) 

#### METHODOLOGY <br>

<pre>
Installed the below required software tools in instances running in AWS

* Apache Kafka
* Apache Storm
* MongoDB
* Flask
* D3

- Streaming data is grabbed from Twitter API using the library tweepy
- The grabbed streaming data is then loaded into the Kafka message queue 
- Apache Storm then grabs data from Kafka using a spout and emits the data in bolt 
- Raw Twitter data in the bolt is then parsed to retrieve the required fields for the project
- Sentimental analysis is then done on this extracted data and the result is loaded into mongodb
- The front end talks with the mongodb to display the appropriate color for each emotion of all the 
states within the United States
</pre>

#### SENTIMENT ANALYSIS

<pre>
* Our sentiment analysis began by creating a list of keywords for each of our emotions 
* We ended up compiling 214 words to represent our five emotions 
and used these keywords to filter the stream of tweets 
* The stream of tweets is then filtered again in Storm against the list of keywords to test the relevance 
of the tweet to the actual emotion it is portraying
* Once all of the tweets were in the database, each emotion had a counter for the number of happy, sad, 
angry, loving, or fearful tweets, and the emotion with the highest count would display its color on the 
map for each state in the United States
</pre>
![alt tag](https://cloud.githubusercontent.com/assets/16888595/25352117/1189636c-28e8-11e7-87cd-0b3dc20c6ed7.png)

#### REFERENCES <br>
<pre>
* http://buscartrabajo.com/files/2011/05/emoticons-thumb.png <br>
</pre>






