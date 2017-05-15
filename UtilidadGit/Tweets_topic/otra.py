import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
from kafka.errors import KafkaError
producer = KafkaProducer(bootstrap_servers='localhost:9092')

CONSUMER_KEY = '35XN6rmuay7ufJX57OfPKUfkY'
CONSUMER_SECRET = 'dakuxOx6Dd4n2QkNPSv6ZzRma9NK8amOqTCuxSOympdwzeX2P4'
ACCESS_KEY_TOKEN = '237553414-pmSc80sy29u1NRaG4Xd5lwHODz5mRsb8avRGJjxz'
ACCESS_SECRET_TOKEN = 'W7wSJDd4mUKWA53vxJoulFX3QJKVkAsy0wq4sLRt1fSii'

class Listener(StreamListener):
    def on_error(self, status_code):
      if status_code == 420:
       #returning False in on_data disconnects the stream
          return False 

    def on_data(self, data):
        json_load = json.loads(data)
        tuit_str = json.dumps (json_load, sort_keys = True, indent = 4, separators=[",",":"])
      #texts=json_load['text']
      #print(texts)
        print(tuit_str)
        producer.send('mitopico', tuit_str.encode()) 


print("---Leyendo Tweets-----")
if __name__ == '__main__':
 escucha = Listener()
 auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
 auth.set_access_token(ACCESS_KEY_TOKEN, ACCESS_SECRET_TOKEN)
 stream = Stream(auth, escucha)
 stream.filter(track=['trance'])