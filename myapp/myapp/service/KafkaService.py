
import pickle
from kafka import KafkaProducer


class KafkaService:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
   
    def send_message(self,title, content):
        message = {
            "title":title,
            "content":content
        }
        serialized_data = pickle.dumps(message, pickle.HIGHEST_PROTOCOL)
        self.producer.send('avia', serialized_data)
        