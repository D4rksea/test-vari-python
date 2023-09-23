conto=110
dec=0
while dec!=1 or dec!=2:
    dec1=input("inserisci 1 se vuoi depositare, 2 per prelevare: ")
    if dec1.isnumeric() == True:
        dec=int(dec1)
        break
    else:
        print("inserisci uno dei numeri, te lo richiedo:")
        dec=0
prel=0
if dec==2:
    prel1=input("inserisci quanti soldi vuoi prelevare ")
    if prel1.isnumeric() == True:
        prel=float(prel1)
    else:
        while prel1.isnumeric() == False:
            print("non è un numero")
            prel1=input("inserisci quanti soldi vuoi prelevare ")
            prel=float(prel1)            
    while conto<prel:
        print("Conto insufficiente per eseguire l'operazione")
        prel1=input("inserisci un prelievo minore: ")
        prel=float(prel1)
conto=conto-prel
#print("Il conto residuo è:")
#print(conto)

dep=0
if dec==1:
    dep1=input("inserisci quanti soldi vuoi depositare ")
    if dep1.isnumeric() == True:
        dep=float(dep1)
    else:
        while dep1.isnumeric() == False:
            print("non è un numero")
            dep1=input("inserisci quanti soldi vuoi depositare ")
            dep=float(dep1)

conto=conto+dep
print("Il conto residuo è:")
print(conto)