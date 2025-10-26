class Person:
    def __init__(self, age: int = 0, name: str = ""):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, value: str):
        self.__name = value

    def get_age(self):
        return self.__age
    
    def set_age(self, value: int):
        self.__age = value

    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
class Moto:
    def __init__(self):
        self.cliente: Person | None = None
        self.time:int = 0
        self.potencia: int = 1
    
    def enter(self, cliente: Person):
        if self.cliente !=None:
            print("fail: busy motorcycle")
            return
        self.cliente = cliente
    
    def leave(self) -> Person | None:
        if self.cliente == None:
            print("fail: empty motorcycle")
            return None
        cliente_passado: Person = self.cliente
        self.cliente = None
        return f"{cliente_passado}"
    
    def buy(self, increment: int):
        self.time += increment
        return
    
    def drive(self, duration: int):
        if self.time == 0:
            print("fail: buy time first")
            return
        if self.cliente == None:
            print("fail: empty motorcycle")
            return
        if self.cliente.get_age() > 10:
            print("fail: too old to drive")
            return
        if duration > self.time:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0
            return
        self.time -= duration

    def honk(self):
        print("P" + "e" * self.potencia + "m")
    
    def init (self, potencia: int = 1):
        self.cliente = None
        self.time = 0
        self.potencia = potencia
        return
    
    def __str__(self):
        cliente_str = "empty" if self.cliente == None else self.cliente
        return f"power:{self.potencia}, time:{self.time}, person:({cliente_str})"


def main():
    motoca = Moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break

        elif args[0] == "init":
            potencia = int(args[1])
            motoca.init(potencia)

        elif args[0] == "honk":
            motoca.honk()

        elif args[0] == "enter":
            name = args[1]
            age = int (args[2])
            motoca.enter(Person(age, name))

        elif args[0] == "buy":
            increment = int(args[1])
            motoca.buy(increment)

        elif args[0] == "leave":
            cliente = motoca.leave()
            if cliente:
                print(f"{cliente}")
        
        elif args[0] == "drive":
            duration = int(args[1])
            motoca.drive(duration)

        elif args[0] == "show":
            print(motoca)

main()