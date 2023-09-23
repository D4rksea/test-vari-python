conto=110
prel=10
while conto<prel:
    prel1=input("inserisci quanti soldi vuoi prelevare ")
    if prel1.isnumeric() == True:
        prel=float(prel1)
        print(prel1+" prel")
        break
    else:
        print("Inserisci un numero, te lo richiedo:")
        prel=100000000000000000
if conto>prel:
    print("conto insufficiente per eseguire l'operazione")
else:
    conto-prel
print(conto)
print(prel1+" prel")