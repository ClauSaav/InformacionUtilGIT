import json
#import elasticsearch as es
import tweepy as tpy
#from kafka import KafkaProducer
#from kafka.errors import KafkaError

#producer = KafkaProducer(bootstrap_servers='localhost:9092')


class Listener(tpy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_status(self, data):
        # When a tweet is published it arrives here.
        print(data.text)
        
        
#            future = producer.send('test', bytes(data.text, 'utf-8'))

#            try:
#                record_metadata = future.get(timeout=10)
                
            



#            except KafkaError:
                        # Decide what to do if produce request failed...
#                            log.exception()
#                            pass

CONSUMER_KEY = '5SV6XgzYO8ddbbS4vnUv3noYt'
CONSUMER_SECRET = 'sQ80VoXyEyovd9SEwR0teaXg4JFiIRrr1a9fxOPz6rjvNv90nT'
ACCESS_KEY = '1661486214-wTnBKyYyykYIiRqwhLFtRSoXj70Zep6dYr6JdFS'
ACCESS_SECRET = 'EkXBBDJFnLl4eU4hza8JmgPFKmKOK2bd6llVSnKCzddHp'
auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tpy.API(auth)


print("===== Tweets en tiempo real =====")


                # Connect to the stream
print(">> Listening to tweets about #python:")
escucha = Listener()
Stream = tpy.Stream(auth=api.auth, listener=escucha)
Stream.filter(track=['BBVA', 'BANCOMER', 'VLA', 'CDMX'])
               
