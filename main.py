print("Digite o ano que nasceu")
A1 = int(input("> "))
print("Digite sua idade atual")
IdadeAtual = int(input("> "))
print("Digite o ano que você que testa")
A2 = int(input("> "))
print("Digite seu nome")
Nome = input("> ")
A3 = A2-A1+IdadeAtual

print (("{},").format(Nome),("no ano de {}").format(A2),("você terá {} anos".format(A3)))
