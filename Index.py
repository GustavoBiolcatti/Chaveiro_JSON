from Chaveiro import Chave

print("***************************")
print("     CHAVEIRO VITÓRIA      ")
print("***************************")

print("******** OPERAÇÕES ********\n"
      "1 - Cadastrar\n"
      "2 - Consultar\n"
      "3 - Alterar\n"
      "4 - Imprimir nota\n"
      "***************************\n")

op = int(input("Operação: "))

chave = Chave()
if op == 1:
    chave.insertChave()

elif op == 2:
    cod = input("Digite o código da chave: ")
    res = chave.getChave(cod)

    for k, v in res.items():
        print("{:10}: {}".format(k.upper(), v))

elif op == 3:
    print("\n***************************\n"
          "1 - Fabricante\n"
          "2 - Tipo\n"
          "3 - Estoque\n"
          "***************************\n")

    op = int(input("Operação: "))

    if op == 1:
        chave.updateFabricante()
    elif op == 2:
        chave.updateTipo()
    elif op == 3:
        chave.updateEstoque()

elif op == 4:
    chave.emiteNota()
