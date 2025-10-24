class Roupa:
    def __init__(self):
        self.__tamanho = ""
    
    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self,valor:str):
        tamanhosValidos = ["PP","P","M","G","GG","XG"]

        if valor not in tamanhosValidos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        
        self.__tamanho = valor

roupa = Roupa()

while True:
        line = input()
        args: list[str] = line.split(" ")
        print(f"${line}")

        match args[0]:
            case "show":
                print(f"size: ({roupa.getTamanho()})")
                
            case"size":
                roupa.setTamanho(args[1].upper())

            case "end":
                break

            case _:
                print("fail: comando invalido")