import pymongo as mon
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('mitopico')
client = mon.MongoClient('54.174.5.92',27017)

#nombre de mi bd
db = client.clautw
tweet = db.tweet 

for msg in consumer:
    raw = msg.value.decode('utf8')
    doc = json.loads(raw)
    del doc['text']
    
    try:
        print("Insertando metadata de: "+str(doc['entities']['user_mentions'][0]['name']))
    except:
        print('Usuario sin nombre')
       
    try:
        res = tweet.insert_one(doc)
    except:
        print("Error al insertar a mongo")