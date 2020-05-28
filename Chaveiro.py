import json


class Chave:
    def __init__(self):
        pass

    def insertChave(self):
        with open("database.json", "r") as arq:
            db = json.load(arq)

            qtd = int(input("Quantidade de chaves a serem cadastradas: "))
            data = {}

            for i in range(0, qtd):
                self.cod = input("\nCódigo: ")

                if self.cod in db:
                    print("A chave informada já se encontra no sistema!")
                else:
                    self.fabricante = input("Fabricante: ").upper()
                    self.tipo = input("Tipo: ").upper()
                    self.estoque = int(input("Estoque: "))

                    data[self.cod] = {
                        "codigo": self.cod,
                        "fabricante": self.fabricante,
                        "tipo": self.tipo,
                        "estoque": self.estoque
                    }

            db.update(data)
            with open("database.json", "w") as arq:
                json.dump(db, arq)

    def getChave(self, cod):
        with open("database.json", "r") as arq:
            db = json.load(arq)

            if cod not in db:
                print("Chave não está cadastrada")
                return 0
            else:
                return db[cod]
                '''for k, v in db[cod].items():
                    print("{:10}: {}".format(k.upper(), v))'''

    def getValor(self, tipo):
        if tipo == "NORMAL":
            valor = 8
        elif tipo == "TETRA":
            valor = 20
        else:
            valor = 0

        return valor

    def updateEstoque(self):
        print("1 - Adicionar\n"
              "2 - Retirar\n"
              "--------------\n"
              "3 - Redefinir\n")

        op = input("Opção: ")
        cod = input("")

        if op == 1:
            qtd = int(input("Quantia a ser adicionada: "))

            with open("database.json", "r") as arq_l:
                db = json.load(arq_l)

                if cod in db:
                    db[cod]["estoque"] += qtd
                else:
                    print("Chave não cadastrada!")

                with open("database.json", "w") as arq:
                    json.dump(db, arq)
        elif op == 2:
            qtd = int(input("Quantia a ser retirada: "))

            with open("database.json", "r") as arq_l:
                db = json.load(arq_l)

                if cod in db:
                    db[cod]["estoque"] -= qtd
                else:
                    print("Chave não cadastrada!")

                with open("database.json", "w") as arq:
                    json.dump(db, arq)
        elif op == 3:
            qtd = int(input("Quantia do estoque: "))

            with open("database.json", "r") as arq_l:
                db = json.load(arq_l)

                if cod in db:
                    db[cod]["estoque"] = qtd
                else:
                    print("Chave não cadastrada!")

                with open("database.json", "w") as arq:
                    json.dump(db, arq)
    
    def updateFabricante(self):
        cod = input("Código: ")
        n_fab = input("Novo fabricante: ").upper().strip()
        
        with open("database.json", "r") as arq_l:
            db = json.load(arq_l)

            if cod in db:
                db[cod]["fabricante"] = n_fab

                with open("database.json", "w") as arq:
                    json.dump(db, arq)
            else:
                print("Chave não cadastrada!")

    def updateTipo(self):
        cod = input("Código: ")
        n_tipo = input("Novo tipo: ").upper().strip()

        with open("database.json", "r") as arq_l:
            db = json.load(arq_l)

            if cod in db:
                db[cod]["tipo"] = n_tipo

                with open("database.json", "w") as arq:
                    json.dump(db, arq)
            else:
                print("Chave não cadastrada!")

    def emiteNota(self):
        tot = int(input("\nQuantia de chaves feitas: "))
        global cont

        with open("database.json", "r") as arq_l:
            db = json.load(arq_l)
            cont = str(db["contador"]) + ".txt"

            with open("database.json", "w") as arq:
                db["contador"] += 1
                json.dump(db, arq)

        with open(cont, "w") as nota:
            nota.write("*************************************\n")
            nota.write("{:^37}".format("CHAVEIRO VITORIA"))
            nota.write("\n*************************************")
            nota.write("\n{:^8} | {:^6} | {:^8} | {:^6}\n\n".format("QUANTIA", "MODELO", "TIPO", "VALOR"))

            for i in range(0, tot):
                qtd = int(input("\nQuantia chave {}: ".format(i+1)))
                cod = input("Código: ")

                chave = self.getChave(cod)

                nota.write("{:^8} | {:^6} | {:^8} | {:^6.2f}\n".format(qtd, chave["codigo"], chave["tipo"], qtd*self.getValor(chave["tipo"])))

                with open("database.json", "r") as arq_l:
                    db = json.load(arq_l)

                    with open("database.json", "w") as arq:
                        db[cod]["estoque"] -= qtd
                        json.dump(db, arq)
