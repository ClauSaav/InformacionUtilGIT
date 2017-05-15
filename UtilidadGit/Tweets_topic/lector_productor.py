from kafka import KafkaProducer
import tweepy as tpy
import limpieza as lm
import conteo as c
import json

class Listener(tpy.StreamListener):

	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False

	def on_data(self, data):
		# Preparando datos para elastic
		#raw = str(status._json)
		raw = json.loads(data)
		data1 = json.dumps(raw, sort_keys =True, indent=4, separators=[",", ":"])
		print(raw['text'])

		# Preparandoos para mongodb
		raw['palabra'] = c.maximo(str(raw['text']))
		del raw['text']
		data2 = json.dumps(raw, sort_keys =True, indent=4, separators=[",", ":"])	

		try:
			Efuture = producer.send('topiclau', str.encode(data1))
			Mfuture = producer.send('topicmongo', str.encode(data2))

		except:
			print("Error codificacion")
	

CONSUMER_KEY = '35XN6rmuay7ufJX57OfPKUfkY'
CONSUMER_SECRET = 'dakuxOx6Dd4n2QkNPSv6ZzRma9NK8amOqTCuxSOympdwzeX2P4'
ACCESS_KEY_TOKEN = '237553414-pmSc80sy29u1NRaG4Xd5lwHODz5mRsb8avRGJjxz'
ACCESS_SECRET_TOKEN = 'W7wSJDd4mUKWA53vxJoulFX3QJKVkAsy0wq4sLRt1fSii'

auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True

auth.set_access_token(ACCESS_KEY_TOKEN, ACCESS_SECRET_TOKEN)
api = tpy.API(auth)


print("**** Tweets en TR ****")

#Start Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Connect to the stream
print("**** Mostrando Tweets: ****")
escucha  = Listener()
Stream = tpy.Stream(auth=api.auth, listener=escucha)
Stream.filter(track=['trance','asot','abgt'], languages=["es"])






#PRIMERO
#import json
#import tweepy as tpy
#from kafka import KafkaProducer
#from kafka.errors import KafkaError

#producer = KafkaProducer(bootstrap_servers='localhost:9092')


#class Listener(tpy.StreamListener):

#    def on_error(self, status_code):
#        if status_code == 420:
#            #returning False in on_data disconnects the stream
#            return False

#    def on_status(self, data):
        # When a tweet is published it arrives here.
#        print(data.text)

#        future = producer.send('topiclau', bytes(data.text, 'utf-8'))

#        try:
#        	record_metadata = future.get(timeout=10)
#        except KafkaError:
        		# Decide what to do if produce request failed...
#        		log.exception()
#        pass

#CONSUMER_KEY = '35XN6rmuay7ufJX57OfPKUfkY'
#CONSUMER_SECRET = 'dakuxOx6Dd4n2QkNPSv6ZzRma9NK8amOqTCuxSOympdwzeX2P4'
#ACCESS_KEY = '237553414-pmSc80sy29u1NRaG4Xd5lwHODz5mRsb8avRGJjxz'
#ACCESS_SECRET = 'W7wSJDd4mUKWA53vxJoulFX3QJKVkAsy0wq4sLRt1fSii'
#auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.secure = True
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tpy.API(auth)


#print("===== Tweets en tiempo real ABRIL =====")


                # Connect to the stream
#print(">> Listening to tweets about #python:")
#escucha = Listener()
#Stream = tpy.Stream(auth=api.auth, listener=escucha)
#Stream.filter(track=['trance'])
               
