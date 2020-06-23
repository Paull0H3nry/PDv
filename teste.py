

i = 0
ii = 1
caixa = float(input("Valor inicial do caixa: "))
op = input("Qual a operação desejada? A = Abrir ou F = Fechar\nOperação: ")
oper = op.upper()
while oper != "A" and oper != "F":
    print("\nOperação inválida!")
    op = input("Qual a operação desejada? A = Abrir ou F = Fechar\nOperação: ")
    oper = op.upper()
    
if oper == "A":
    while i == 0:
        print("\nValor inicial do caixa %.2f" % caixa)
        op = input("Começar vendas? S = (Sim) ou F = (Fechar)\nOperação: ")
        oper = op.upper()
        while oper != "S" and oper != "F":
            print("\nERROR!")
            op = input("Começar vendas? S = (Sim) ou F = (Fechar)\nOperação: ")
            oper = op.upper()
        if oper == "S":
            print("\nBORA VENDER MEU POVO!!\n")
            while i == 0:
                venda = float(input("Valor da %dº venda: "% ii))
                ii = ii + 1
                if venda == 34565621:
                    break
                caixa = caixa + venda
                
            break
        
        else:
            break

else:
    print("\nValor final do caixa %.2f" % caixa)


print("\nValor final do caixa %.2f" % caixa)
