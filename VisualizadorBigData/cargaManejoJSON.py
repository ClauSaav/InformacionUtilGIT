#importando la libreria
import json

#Cargando JSON y decodificando
jasonSTR = '{ "cuentaUsuarios" : 3, "usuarios" : [{"nombre" : "Marcos", "status" : "online"},{"nombre" : "Claudia", "status" : "online"}]}'
jasonDECOD = json.loads(jasonSTR)
print(jasonDECOD ["cuentaUsuarios"])

usuarios = jasonDECOD["usuarios"]
print(usuarios)

#FORMA 1 DE IMPRESION
#usuario0 = usuarios[0]
#usuario1 = usuarios[1]
#print(usuario0)
#print(usuario1)

#print(usuario0["nombre"])
#print(usuario1["status"])

#print(jasonDECOD["usuarios"][1]["nombre"])
#print(jasonDECOD["usuarios"][1]["status"])

#FORMA 2 DE IMPRESION DEL CONTENIDO EN JSON 
for usuario in usuarios:
	print(str(usuario["nombre"])+", "+str(usuario["status"]))



