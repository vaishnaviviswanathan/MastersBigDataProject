# Using kafka-python opensource library

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['172.31.43.251:9092'])

# Asynchronous by default
producer.send('twitter1', b'raw_bytes')
