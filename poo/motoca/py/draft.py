class Person:
    def __init__(self, age: int = 0, name: str = ""):
        self.__age = age
        self.__name = name

        def __str__(self):
            return f"{self.getName()}:{self.getAge()}" 
        
        def getAge(self) -> int:
            return self.__age
        
        def getName(self) -> str:
            return self.__name
        