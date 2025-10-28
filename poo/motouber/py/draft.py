class Person:
    def __init__(self, name: str, money: int = 0):
        self.__name = name
        self.__money = money
    
    def get_name(self):
        return self.__name
    
    def set_name(self, value: str):
        self.__name = value
    
    def get_money(self):
        return self.__money

    def set_money(self, value: int):
        self.__money = value

    def __str__(self):
        return f"{self.__name}:{self.__money}"
    
class Motouber:
    def __init__(self):
        self.__cost: int = 0
        self.__driver: Person | None = None
        self.__passenger: Person | None = None

    def get_cost(self):
        return self.__cost
    
    def set_cost(self, value: str):
        self.__cost = value

    def get_driver(self):
        return self.__driver
    
    def set_driver(self, value: int):
        self.__driver = value

    def get_passenger(self):
        return self.__passenger
    
    def set_passenger(self, value: int):
        self.__passenger = value

    def __str__(self):
        driver_str = self.__driver if self.__driver else "None"
        passenger_str = self.__passenger if self.__passenger else "None"   
        return f"Cost: {self.__cost}, Driver: {driver_str}, Passenger: {passenger_str}"
        
    def set_motorista(self, driver: Person):
        if self.__driver is not None:
            print("fail: ja existe um motorista")
            return
        self.__driver = driver

    def set_passageiro(self, passenger: Person):
        if self.__passenger is not None:
            print("fail: moto ocupada")
            return
        self.__passenger = passenger

    def car(self, value: int):
        self.__cost += value
    
    def leavePass(self):
        if self.__passenger is None:
            print("fail: nao ha passageiro")
            return
        
        passAntes: Person = self.__passenger

        if self.__passenger.get_money() < self.__cost:
            print("fail: Passenger does not have enough money")
            self.__driver.set_money(self.__driver.get_money() + self.__cost)
            
            self.__passenger.set_money(0)
            self.__cost = 0
            self.__passenger = None
            print(f"{passAntes} left")
            return
        
        self.__passenger.set_money(self.__passenger.get_money() - self.__cost)
        self.__driver.set_money(self.__driver.get_money() + self.__cost)
        self.__cost = 0
        self.__passenger = None
        print(f"{passAntes} left")
    
def main():
    motouber = Motouber()
    
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
            break

        elif args[0] == "show":
            print(motouber)

        elif args[0] == "setDriver":
            driver = args[1]
            money_driver = int(args[2])
            motouber.set_motorista(Person(driver, money_driver))

        elif args[0] == "setPass":
            passenger = args[1]
            money_pass = int(args[2])
            motouber.set_passageiro(Person(passenger, money_pass))
    
        elif args[0] == "drive":
            km = int(args[1])
            motouber.car(km)

        elif args[0] == "leavePass":
            motouber.leavePass()
main()


    

        


   
        
