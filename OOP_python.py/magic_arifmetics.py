# __add__() - для операций "+" сложения
# __sub__() - для операций "-" вычитания
# __mul__() - для операций "*" умножения
# __truediv__() - для операций "/" деления

class Clock: 

    __day = 86400

    def __init__(self, seconds : int):
        if not isinstance(seconds, int):
            raise TypeError("секунды должны быть целым числом")
        self.seconds = seconds % self.__day
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)} : {self.__get_formatted(m)} : {self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0") # добавляем незначащий ноль справа (rjust)

    def __add__(self, other):
        if not  isinstance(other, (int,Clock)):
            raise ArithmeticError("в добавляемом параметре должен быть int или clock")
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds + sc)

    def __radd__(self, other): # если экземпляр класса clock будет записан справа от оператора сложения
        return self + other
    
    def __iadd__(self, other): # чтобы не создавался новый экземпляр класса clock 
        if not isinstance(other, Clock):
             raise ArithmeticError("в добавляемом параметре должен быть int или clock")
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        
        self.seconds += sc
        return self
        
    
c1 = Clock(1000)
c2 = Clock(2000)
c3 = Clock(4000)

c1.seconds = c1.seconds + 100

c1 = c1 + 100 # __add__ сработал 
c4 = c1 + c2 + c3 # __add__ сработал 

c3 = 100 + c3 # __radd__ сработал вместе с __add__

c2 += 100 # __iadd__ сработал 

print(c4.get_time())

print(c3.get_time())
print(c2.get_time())