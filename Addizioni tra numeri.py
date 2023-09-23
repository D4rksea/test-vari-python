numero1=input("inserisci cortesemente il primo numero: ")
numero2=input("inserisci cortesemente il secondo numero: ")
numero1=float(numero1)
numero2=float(numero2)

somma=numero1+numero2
differenza=numero1-numero2
divisione=numero1/numero2
resto=numero1%numero2
moltiplicazione=numero1*numero2

som=str(somma)
dif=str(differenza)
div=str(divisione)
rest=str(resto)
molt=str(moltiplicazione)

print("la somma è: "+som)
print("la differenza è: "+dif)
print("la divisione è: "+div+" con un resto pari a: "+rest)
print("la moltiplicazione è: "+molt)