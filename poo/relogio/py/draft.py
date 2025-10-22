class Watch:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.__hour = 0;
        self.__minute = 0;
        self.__second = 0;
    
        self.set_hour(hour);
        self.set_minute(minute);        
        self.set_second(second);

    def __str__ (self) -> str:
        hour = self.get_hour();
        minute = self.get_minute();
        second = self.get_second();    
        return f"{hour:02}:{minute:02}:{second:02}";

    def get_hour(self) -> int:
        return self.__hour;

    def get_minute(self) -> int:
        return self.__minute;
    
    def get_second(self) -> int:
        return self.__second;

    def set_hour(self, value: int):
        if value < 0 or value >23:
            print("fail: hora invalida");
            return;
        self.__hour = value;
    
    def set_minute(self, value: int):
        if value < 0 or value >59:
            print("fail: minuto invalido");
            return;
        self.__minute = value;
    
    def set_second(self, value: int):
        if value < 0 or value >59:
            print("fail: segundo invalido");
            return;
        self.__second = value;

    
    def next_second(self):
        if self.__second != 59:
            self.__second += 1;
        else:
            self.__second = 0
            if self.__minute != 59:
                self.__minute +=1;
            else:
                self.__minute = 0;
                if self.__hour != 23:
                    self.__hour +=1;
                else:
                    self.__hour =0;

def main ():
    watch= Watch();
    while True:
        line = input();
        args = line.split(" ");
        print(f"${' '.join(args)}");

        match args[0]:
            case "show":
                print(watch);
            case "init":
                watch = Watch(int(args[1]), int(args[2]), int(args[3]));
            case "set":
                watch.set_hour(int(args[1]));
                watch.set_minute(int(args[2]));
                watch.set_second(int(args[3]));
            case "next":
                watch.next_second();
            case "end":
                break;
            case _:
                print("fail: comando invalido");
main();

       





    
