class Chinela:
    def __init__(self):
        self.__size = 0;
    
    def get_size(self) -> int:
        return self.__size;

    def set_size(self, valor: int):
        if valor < 20 or valor > 50 or valor % 2 !=0:
            print("fail: tamanho invalido");
            return;
        self.__size = valor;

def main():
        chinela = Chinela();
        
        while chinela.get_size() == 0:
            try:
                entrada = int(input("Digite o tamanho da chinela (20 a 50, pares apenas): "))
                chinela.set_size(entrada);
            except ValueError:
                  print("fail: valor invalido");
                  

        print(f"Sua numeração de chinela tem o tamanho: {chinela.get_size()}")

main()