
"""
@author IanGarcia, David

Realiza la suma de los numeros naturales considerandolos n>0
en caso de que n<=0 lanzara una advertencia en forma de string 
y la regresara
"""
def sumToN(natural):
	n=int(natural)
	if(natural<=0):
		print('Considera a los naturales: n>0')
		return "Failure considered"
	return int(int((n+1)*n)/2)

#Imprimimos el resultado de sumar los primeros 100 naturales
print(sumToN(100))
