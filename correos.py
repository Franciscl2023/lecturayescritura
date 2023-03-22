#este programa crea correos:
#Lista de nombres y apellidos.
nombres=["adrian","francisco","sarahi","segio","aurelio"]
apellidos=["hernandez","perez","patricio","lezama","hernandez"]
correos=[]
#checar que sean de igual tamaño
ln=len(nombres)
la=len(apellidos)
if ln ==la:
    #abrir archivo
    lista=open("lista.txt","w")
    for i in range(ln):
     correo=nombres[i]+ "."+apellidos[i]+"@correo.com"
     correos.append(correo)
     print(correo)
for x in range(ln):
    lista.write(correos[x])
    lista.write("\n")
lista.close()
            
           
