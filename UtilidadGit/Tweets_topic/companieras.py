import json
#import elasticsearch as es
import tweepy as tpy


class Listener(tpy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_status(self, data):
        # When a tweet is published it arrives here.
        print(data.text) 

CONSUMER_KEY = 'u4hbs7izOaPdqU8pNOm4Djp8z'
CONSUMER_SECRET = 'zEK37gI0cojk9eE4wvUcQxGSYAFm8tTjsFqloXK8LZaeoOj5aq'
ACCESS_KEY = '237553414-MmqJairVwZJreYfOR7k7lnbQsaIFAEJrKmsnooLE'
ACCESS_SECRET = 'jRCwo4Pp1RTkPqGuhSDzzEEtK5qnsLXgrp1qeUR0jSHDd'

auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tpy.API(auth)


print("===== Tweets en tiempo real =====")


# Connect to the stream
print(">> Listening to tweets about #python:")
escucha  = Listener()
Stream = tpy.Stream(auth=api.auth, listener=escucha)
Stream.filter(track=['ASOT', 'BBVA', 'trance', '#asot807', 'jajajajaja', '#viral'])
