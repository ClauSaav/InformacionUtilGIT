import facebook
import requests

token = ""
graph = facebook.GraphAPI(token)
cantidadComentarios = 100
PageId = ''

CuentaComentarios = 0
ListaComents = []

bandera = False

coments = graph.get_connectios(PageId, 'feed')

while  True:
	try:
		for coment in coments['data']:
			ListaComent = []
			try:
				mensaje = coment['message']
	except KeyError:
		continue
	print(mensaje)
	ListaComent.append(mensaje)
	ListaComents.append(ListaComent)
	CuentaComentarios = CuentaComentarios + 1
	print("")
	if(CuentaComentarios >= cantidadComentarios):
		bandera = True
		break
		if(bandera):
			break
			coments = requests.get(coments['paging']['next']).json()
		except KeyError:
			break
