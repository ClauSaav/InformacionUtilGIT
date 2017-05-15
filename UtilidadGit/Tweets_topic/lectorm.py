import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
from kafka.errors import KafkaError
import pandas as pd

producer = KafkaProducer(bootstrap_servers='localhost:9092')

#CONSUMER_KEY = '5SV6XgzYO8ddbbS4vnUv3noYt'
#CONSUMER_SECRET = 'sQ80VoXyEyovd9SEwR0teaXg4JFiIRrr1a9fxOPz6rjvNv90nT'
#ACCESS_KEY_TOKEN = '1661486214-wTnBKyYyykYIiRqwhLFtRSoXj70Zep6dYr6JdFS'
#ACCESS_SECRET_TOKEN = 'EkXBBDJFnLl4eU4hza8JmgPFKmKOK2bd6llVSnKCzddHp'


CONSUMER_KEY = '04MR5CFMcnjsIAltPjuQYKKfz'
CONSUMER_SECRET = 'H0g82bYsfLY7Fdwrfnata5ICwR9AAnoQBlSTC2jo5On7rP7AAg'
ACCESS_KEY_TOKEN = '768207640899964928-PSbWvLHpV21i0s525GNblAp07A1Zus1'
ACCESS_SECRET_TOKEN = 'O21kJb3KwMfIbPdj7bTWUndoATCesFBKQwRCR8Is4otxe'

class Listener(StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_data(self, data):
       json_load = json.loads(data)
       texts=json_load['text']
       print (texts)
        # When a tweet is published it arrives here.
       	#print(data.text)
       producer.send('streams-file-input', texts.encode())
       







 # Connect to the stream
print("-O-O-O-O-O-O-Leyendo Tweets-O-O-O-O-O-O-O")
if __name__ == '__main__':
  escucha = Listener()
  auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY_TOKEN, ACCESS_SECRET_TOKEN)
  stream = Stream(auth, escucha)
  stream.filter(track=['MEXICO','hola'])
