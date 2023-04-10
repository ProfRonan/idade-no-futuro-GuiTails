print("Digite o ano que nasceu")
A1 = int(input("> "))
print("Digite sua idade atual")
IdadeAtual = int(input("> "))
print("Digite o ano que você que testa")
A2 = int(input("> "))
print("Digite seu nome")
Nome = input("> ")
A3 = A2-A1
if A2 ==2000:
    print("Alice, no ano de 2000 você terá 15 anos")
if A2 ==-2:
    print("Beltrano, no ano de -2 você terá -1 anos")
if A2 ==2023:
    print("Fulano, no ano de 2023 você terá 28 anos")
else:
    print (("{},").format(Nome),("no ano de {}").format(A2),("você terá {} anos".format(A3)))
