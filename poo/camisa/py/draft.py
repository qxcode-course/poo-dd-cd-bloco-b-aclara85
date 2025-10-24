class Camisa:
 def __init__(self):
    self.__tamanho = ""

 def getTamanho(self) -> str:
    return self.__tamanho

 def setTamanho(self, valor:str):
    tamanhosValidos = ["PP","P","M","G","GG","XG"]
    valor = valor.upper()

    if valor not in tamanhosValidos:
        print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        return
    
    self.__tamanho = valor
    
camisa = Camisa()

while camisa.getTamanho() == "":
    print("Digite o seu tamanho de roupa:")
    tamanho = input()
    camisa.setTamanho(tamanho)
print(f"Tamanho definido como: {camisa.getTamanho()}")
