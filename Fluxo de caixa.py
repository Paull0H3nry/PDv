from datetime import datetime
while True:
    from time import sleep
    try:
        inicial = open("Caixa.txt","x")
        inicial.close()
        inicial = open("Caixa.txt","w+")
        inicial.write("0")
        inicial.close()
    except FileExistsError:
        inicial = open("Caixa.txt","r+")
        pcaixa = inicial.read()
        print("Valor inicial do caixa R$", pcaixa)
        inicial.close()
    else:
        inicial = open("Caixa.txt","r+")
        pcaixa = inicial.read()
        print("Valor inicial do caixa R$", pcaixa)
        inicial.close()
    i = 0
    total = 0
    ii = 1
    caixa = float(pcaixa)
    print("Hoje é",datetime.today().strftime('%d-%m-%Y'))
    op = input("Qual a operação desejada? A = Abrir ou F = Fechar\nOperação: ")
    oper = op.upper()
    while oper != "A" and oper != "F":
        print("\nOperação inválida!")
        op = input("Qual a operação desejada? A = Abrir ou F = Fechar\nOperação: ")
        oper = op.upper()

    if oper == "A":
        while i == 0:
            op = input("Começar vendas? S = (Sim) ou F = (Fechar)\nOperação: ")
            oper = op.upper()
            while oper != "S" and oper != "F":
                print("\nERROR!")
                op = input("Começar vendas? S = (Sim) ou F = (Fechar)\nOperação: ")
                oper = op.upper()
            if oper == "S":
                print("\nBom dia!\n")
                print("Escreva somente NÚMEROS\nUse o PONTO em vez da vírgula, para números decimais.\nCaso o programa feche inesperadamente, é só abrir ele novamente\n(ficará salvo o último progresso válido)\n")
                while i == 0:
                    venda = float(input("Valor da %dº venda: "% ii))
                    ii = ii + 1
                    if venda == 34565621:
                        break
                    total += venda
                    caixa += venda
                break
            else:
                break
    sleep(1)
    print("\nValor final do caixa %.2f" % caixa)

    final = open("Caixa.txt","w+")
    caixa = str(caixa)
    final.write(caixa)
    final.close()
    try:
        fluxo = open("Fluxo.txt","x")
        inicial.close()
    except FileExistsError:
        fluxo = open("Fluxo.txt","a")
        fluxo.write(datetime.today().strftime('%d-%m-%Y'))
        fluxo.write("\n")
        fluxo.write(str(total))
        fluxo.write("\n\n")
        fluxo.close()
    else:
        fluxo = open("Fluxo.txt","a")
        fluxo.write(datetime.today().strftime('%d-%m-%Y'))
        fluxo.write("\n")
        fluxo.write(str(total))
        fluxo.write("\n\n")
        fluxo.close()
    sleep(1)
    input("\n\nPressione qualquer tecla para fechar o programa...")
    break

