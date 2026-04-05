class Trainable: 
    def __init__(self,name,data = []):
        self.name = name
        self.data = data

    def train(self, data):
        print("Обучаюсь на данных...")
        self._trained = True
        return True



class Serializable: 
    def __init__(self,name,data = None):
        self.name = name
        self._data = data if data is not None else []
        self._accuracy = 0.0
    
    def save(self, filename):
        print(f"Сохраняю в {filename}")
        return True
    
    def load(self, filename):
        print(f"Загружаю из {filename}")
        return True


class DataProcessor(Trainable, Serializable):
    def __init__(self,name,data = None):
        self._name = name
        self._data = data if data is not None else []
        self._accuracy = 0.0

    def __str__(self):
        return f"DataProcessor: {self._name} (данных: {len(self._data)})"
    
    def __repr__(self):
        """Вызывается в консоли"""
        return f"DataProcessor('{self._name}')"

    def __len__(self):
        """Вызывается при len(obj)"""
        return len(self._data)
    
    @property
    def data(self):
        return self.data
    
    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self,value):
        if 0 <= self._accuracy <= 1:
            self._accuracy = value
            print(f"Accuracy установлен: {value}")
        else:
            raise ValueError("Акюраси не установлен")
    
processor = DataProcessor("ML-1", [1, 2, 3, 4, 5])

print(processor)           # __str__: DataProcessor: ML-1 (данных: 5)
print(len(processor))      # __len__: 5
print(processor.accuracy)  # @property: 0.0
processor.accuracy = 0.95  # @setter: Accuracy установлен: 0.95
processor.train([1,2,3])   # Из Trainable
processor.save("model.pkl")  # Из Serializabl 
    