from streamparse.spout import Spout
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.client import SimpleClient
import json
from kafka import KafkaConsumer

class WordSpout(Spout):
    outputs = ['message']

    def initialize(self, stormconf, context):
        self.kafka = SimpleClient('172.31.43.251:9092')
#        self.consumer = SimpleConsumer(self.kafka,"my-group","twitter1",fetch_size_bytes=8192,buffer_size=1048576,max_buffer_size=2097152)
        self.consumer = KafkaConsumer('twitter1',group_id='my-group',bootstrap_servers=['172.31.24.2:9092'])

    def next_tuple(self):
            for message in self.consumer:
                self.logger.info([message])
                self.emit([message])
#                self.logger.info([json.dumps(message, default=lambda x: None)])
#                self.emit([json.dumps(message, default=lambda x: None)])

if __name__ == '__main__':
    WordSpout().run()
