caixa_1 = open("Caixa.txt","w+")
caixa_ini = float(input("valor do caixa: "))
caixa_1.write(str(caixa_ini))
caixa_1.close()

caixa_1 = open("Caixa.txt","w")
x = float(input("proximo valor: "))
opr = float(caixa_ini + x)
caixa_1.write(str(opr))
caixa_1.close()

caixa_1 = open("Caixa.txt","r+")
print(caixa_1.read())
