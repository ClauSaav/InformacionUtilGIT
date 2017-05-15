from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from datetime import datetime
import json

consumer = KafkaConsumer('test')
#es = Elasticsearch(["localhost:9200"])
es = Elasticsearch(["http://search-beevagrad-yzavdnk3vgybj33teqgucq7ray.us-east-1.es.amazonaws.com:80"])

print(">> Escuchando Tweets en topiclau:")

for msg in consumer:
	
	raw = msg.value.decode('utf8')
	doc = json.loads(raw)
	
	try:
		print(doc['entities']['user_mentions'][0]['name'])
	except:
		print('Usuario sin nombre')

	try:
		res = es.index(index="clautw", doc_type="topiclau", body=doc)
		print("Estado mensaje: ",res['created'])
	except:
		print('Error al enviar')



#PRUEBA 1
#from datetime import datetime
#from kafka import KafkaConsumer 
#from elasticsearch import Elasticsearch

#consumer = KafkaConsumer('topiclau')

#es = Elasticsearch('http://search-beevagrad-yzavdnk3vgybj33teqgucq7ray.us-east-1.es.amazonaws.com:80')

#for msg in consumer:
#	print (msg.value)
#	doc = {
#               'quien': 'clautw',
#               'text': str(msg.value),
#               'timestamp': datetime.now(),
#		}
#	res = es.index(index="clautw", doc_type='topiclau', body=doc)
