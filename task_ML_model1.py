from abc import ABC, abstractmethod

class MLmodel(ABC):
    def __init__(self,name):
        self._name = name
        self._is_trained = False
    
    @abstractmethod
    def train(self, data):
        pass
    
    @abstractmethod
    def predict(self,x):
        pass

    def get_status(self):
        status = "Готова" if self._is_trained else "Не обучена"
        return f"{self._name}: {status}"
    

class LinearModel(MLmodel):
    def __init__(self, name):
        super().__init__(name)
        self.coef = 0
    
    def set_coef(self,coef):
        self.coef = coef

    def predict(self, x):
        return x * self.coef
    
    def train(self, data):
        self._is_trained = True
        print("im training")
        self.coef = sum(data) / len(data) if data else 0



class TreeModel(MLmodel):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def train(self,data):
        self._is_trained = True
        self.max_depth = len(data)


    def predict(self, x):
        return sum(x) / len(x) if x else 0 


linear = LinearModel("LR-1")
tree = TreeModel("RF-1", max_depth=10)

linear.train([1, 2, 3, 4, 5])
tree.train([1, 2, 3, 4, 5])

print(linear.get_status())  # LR-1: Готова
print(linear.predict(10))   # 30.0

print(tree.get_status())    # RF-1: Готова
print(tree.predict([10, 20, 30])) 



class MLModel:
    def __init__(self, name):
        self._name = name
        self._data = []
    
    def __str__(self):
        # Вызывается при print(obj)
        # Для ЛЮДЕЙ (красивый вывод)
        return f"Модель: {self._name}"
    
    def __repr__(self):
        # Вызывается в консоли без print
        # Для РАЗРАБОТЧИКОВ (точная информация)
        return f"MLModel('{self._name}')"
    
    def __len__(self):
        # Вызывается при len(obj)
        return len(self._data)
    
    def __getitem__(self, index):
        # Вызывается при obj[index]
        return self._data[index]
    
    def __call__(self, x):
        # Вызывается при obj(x)
        return x * 2

# Использование
model = MLModel("LR-1")

print(model)           # Вызывает __str__: "Модель: LR-1"
print(repr(model))     # Вызывает __repr__: "MLModel('LR-1')"
print(len(model))      # Вызывает __len__: 0
model._data = [1,2,3]
print(model[0])        # Вызывает __getitem__: 1
print(model(10))       # Вызывает __call__: 20