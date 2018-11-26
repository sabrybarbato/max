i=0
a=input("inserisci un numero")
a=int(a)
max = a


while i<9:
	a=input("inserisci il secondo numero: ")
	a=int(a)	
	if a>max:
		max=a
	i+=1


print ("il valore max è: ", max)	