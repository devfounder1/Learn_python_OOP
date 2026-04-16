# __eq__() - для равенства ==
# __ne__() - для неравенства "!="
# __it__() - для оператора меньше <
# __le__() - для оператора меньше или равно <=
# __gt__() - для оператора больше > 
# __ge__() - для оператора больше или равно >=

class Clock: 

    __day = 86400

    def __init__(self, seconds : int):
        if not isinstance(seconds, int):
            raise TypeError("секунды должны быть целым числом")
        self.seconds = seconds % self.__day
    
    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("операнд справа должен быть int или clock")
        
        return other if isinstance(other,int) else other.seconds


    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc
    
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

c1 = Clock(1000)
c2 = Clock(1000)

print(c1 > c2)
