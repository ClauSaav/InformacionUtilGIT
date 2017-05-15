import json
import elasticsearch as es
import tweepy as tpy

class Listener(tpy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_status(self, data):
        # When a tweet is published it arrives here.
        print(data.text) 

CONSUMER_KEY = '35XN6rmuay7ufJX57OfPKUfkY'
CONSUMER_SECRET = 'dakuxOx6Dd4n2QkNPSv6ZzRma9NK8amOqTCuxSOympdwzeX2P4'
ACCESS_KEY = '237553414-pmSc80sy29u1NRaG4Xd5lwHODz5mRsb8avRGJjxz'
ACCESS_SECRET = 'W7wSJDd4mUKWA53vxJoulFX3QJKVkAsy0wq4sLRt1fSii'

auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tpy.API(auth)


print("===== Tweets en tiempo real Abril =====")


# Connect to the stream
print(">> Escuchando Tweets en #Python:")
escucha  = Listener()
Stream = tpy.Stream(auth=api.auth, listener=escucha)
Stream.filter(track=['asot'])
