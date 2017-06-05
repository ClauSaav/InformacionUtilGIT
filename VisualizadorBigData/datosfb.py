import facebook 
import request

#llaves de acceso de API
token = ""
graph = facebook.GraphAPI(token)
cantidadComentarios = 100
PageId = '1415691342026378'

cuentaLikes = 0 
cuentaPaginas = 0
cuentaComentarios = 0
ListaComents = []

bandera = False

coments = graph.get_connection(PageId, 'feed')

print(coments)
while True:
	try:
		for coment in coments['data']:
			ListaComent =  []
			try:
				mensaje = coment['message']
			except KeyError
			continue

			cuentaLikes = 0
			print(mensaje)

			while(True):
				try:

					for like in coment['likes']['data']:
						cuentaLikes = cuentaLikes +1
					coment['likes'] = requests.get(coment['likes']['paging']['next']).json()
					except KeyError:
						break

					print(cuentaLikes)
					ListaComent.append(mensaje)
					ListaComent.append(cuentaLikes)
					ListaComents.append(ListaComent)
					cuentaComentarios = cuentaComentarios + 1
					print("")

					if(cuentaComentarios >= cantidadComentarios):
						bandera = True
						break
					if(bandera):
						break
					coments = requests.get(coments['paging']['next']).json()
				except KeyError:
					break