from datetime import datetime
import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from io import StringIO

consumer = KafkaConsumer('mitopico')

es = Elasticsearch(["http://search-beevagrad-yzavdnk3vgybj33teqgucq7ray.us-east-1.es.amazonaws.com:80"])
for msg in consumer:
	json_load= json.loads(msg.value)
	ejson= json.dumps (json_load, sort_keys = True, indent = 4, separators=[",",":"])
	print(ejson) 
	try:
		res = es.index(index="tcl", doc_type='twc', body=ejson)
	except:
		print("Pasa")







