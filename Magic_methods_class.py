# class DataProcessor:
#     def __init__(self,name):
#         self.name = name
#         self.data =[]

#     def add_data(self,value):
#         self.data.append(value)
    
#     def getstatus(self):
#         return{
#             'count' : len(self.data),
#             'sum' : sum(self.data) ,
#             'avg' : sum(self.data)/len(self.data)if self.data else 0 
#         }
    

# proc = DataProcessor("ML-model")
# proc.add_data(10)
# proc.add_data(10)
# print(proc.getstatus())



# class MLmodel:
#     def __init__(self, name):
#         self.name = name
#         self.data = []  # Инициализируем пустым
    
#     def train(self, data):
#         self.data = data  # Сохраняем состояние
    
#     def predict(self, x):  # Без параметра data!
#         # Используем self.data из train()
#         avg = sum(self.data) / len(self.data) if self.data else 0
#         return avg * x

# # Использование
# ML = MLmodel("MLchik")
# ML.train([1, 2, 3, 45, 6, 7, 788, 4])
# print(ML.predict(3))




# class Model:  # Родительский класс
#     def __init__(self, name):
#         self.name = name
    
#     def train(self, data):
#         print(f"{self.name} обучается...")

# class LinearRegression(Model):  # Наследник
#     def __init__(self, name, lr=0.01):
#         super().__init__(name)  # Вызов родителя
#         self.lr = lr
    
#     def train(self, data):  # Переопределение метода
#         print(f"{self.name} обучается с lr={self.lr}")

# class RandomForest(Model):  # Другой наследник
#     def train(self, data):
#         print(f"{self.name} обучает деревья...")

# # Использование
# lr = LinearRegression("LR-1", lr=0.1)
# rf = RandomForest("RF-1")
# lr.train([1,2,3])  # LR-1 обучается с lr=0.1
# rf.train([1,2,3]) 



# class Model():

#     def __init__(self,name,data):
#         self.name = name
#         self.data = data

#     def train(self):
#         self.data = sum(self.data) / len(self.data)
#         return self.data
        
# class LinearlRegression(Model):
#     def __init__(self,name,lr=0.1):
#         super().__init__(name)
#         self.lr = lr
#     def train(self):
#         return sum(self.data) / 10


# class Random_forest(Model):
#     def __init__(self, name, data):
#         super().__init__(name, data)
#     def train(self):
#         self.data = len(self.data) / 100
#         return self.data



# a = Random_forest("ML1", [1,2,3,4,5,6])
# print(a.train())

# b = LinearlRegression("ML2")
# print(b.train())


# class point:
#     color = 'red'
#     circle = 2

#     def __init__(self,x,y):
#         print('выов инит')
#         self.x = x
#         self.y = y

#     def set_cords(self,x, y):
#         self.x = x
#         self.y = y 

#     def get_cords(self):
#         return self.x, self.y
    
#     def __del__(self):
#         print('удаление экземпляра: ' + str(self))

# pt = point(1,2)
# print(pt.__dict__)
    
########################################################################################################################

# class point1:
#     def __init__(self,x,y):
#         print('вызов инит')
#         self.x = x
#         self.y = y
    
#     def __new__(cls, *args, **kwargs):
#         print('вызов new для ' + str(cls))
#         return super().__new__(cls)

        
# pt1 = point1(1,2) 
# print(pt1)



# class DataBase:
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
    
#     def __del__(self):
#         DataBase.__instance = None

#     def __init__(self, user, passw,port):
#         self.user = user
#         self.passw = passw
#         self.port = port

#     def connect(self):
#         print(f"соединение с БД  {self.user}, {self.passw}, {self.port}")


# db = DataBase('alex', '12223', 40)
# db2 = DataBase('oleg','123456', 80)

# db.connect()
# db2.connect()



class point1:
    MAX_COORD = 100
    MIN_coord = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_coord <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    @classmethod
    def set_bound(cls, left):
        cls.MIN_coord = left

    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item) ## неявное наследие от класса object в python
    
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:    
            print("__setattr__: ", value)
            object.__setattr__(self, key, value)

    def __getattr__(self, name): ## обращение к несуществующему экземпляру класса  
        print("__getattr__: ", name)
        return False
    
    def __delattr__(self, name):
        print("__delattr__: " + name)
        object.__delattr__(self, name) ## обязательное обращение к родительскому классу

pt1 = point1(1,2) ## вот тут будет __setattr__ - 2 раза 
pt2 = point1(10,20) ## вот тут будет __setattr__ - 2 раза

a = pt1.x ## обращение к экземпляру класса, __getattribute__

pt1.x = 10  ## вот тут будет __setattr__ - 1 раза

del pt1.x ## здесь будет __delattr__

a = pt1.yy ## несуществующий элемент, тогда будет __getattr__