import pymongo as mon
from kafka import KafkaConsumer
import json



consumer = KafkaConsumer('topicmongo')
mongoClient = mon.MongoClient('172.17.0.2',27017)

# Con. base de datos
db = mongoClient.grad
# Selecciona la coleccion
clautw = db.clautw

for msg in consumer:
	
	raw = msg.value.decode('utf8')
	doc = json.loads(raw)
	
	try:
                print("Metadatos Tweet: "+str(doc['entities']['user_mentions'][0]['name']))
	except:
		print('Usuario sin nombre')
         
	try:
		res = clautw.insert_one(doc)
	except:
print("Error Insertar a mongo")