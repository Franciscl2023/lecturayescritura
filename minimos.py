#este programa realiza la tecnica de minimos cuadrados
# lista de X y Y.
x=[1,2,3,4,5]
y=[4,7,9,12,16]
#tamaño de X y Y
n=len(x)
#suma de valores de X
sumax=0
for i in range(n):
    xv=x[i]
    sumax=sumax+xv
#suma de valores de y
sumay=0
for i in range(n):
    yv=y[i]
    sumay=sumay+xv
print("sumax=()".format(sumax))
print("sumay=()".format(sumay))
#suma de valores de x por y
sumaxy=0
for i in range(n):
    xv=x[i]
    yv=y[i]
    producto=xv*yv
    sumaxy=sumaxy+producto
print("sumaxy{}".format(sumaxy))


