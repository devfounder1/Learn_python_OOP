import math as mt

class stripChars:
    def __init__(self,chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwds):
        print("__call__")
        if not isinstance(args[0], str):
            raise TypeError("аргумент должен  быть строкой")
        
        return args[0].strip(self.__chars)

s1 = stripChars("?:!.; ")
res = s1(" Hello World!? ")
print(res)

s2 = stripChars(" ")
res2 = s2(" Hello World!? ")
print(res2)


class Derivate:
    def __init__(self, func):
        self.__fn = func 

    def __call__(self,x, dx = 0.0001, *args, **kwds):
        return (self.__fn(x+dx) - self.__fn(x)) / dx

@Derivate  # и тогда derivate становится классом декоратором  
def df_sin(x):
    return mt.sin(x)

#df_sin = Derivate(df_sin) # теперь df_sin ссылается на экземпляр класса Derivate
print(df_sin(mt.pi/3))