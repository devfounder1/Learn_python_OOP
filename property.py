class person:
    def __init__(self, name,old):
        self.__old = old
        self.__name = name
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self,old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

p = person('сергей', 20)
print(p.__dict__)


a = p.old ## отработал property и там метод get_old
print(a)

p.old = 45 
del p.old
p.old = 70
print(p.old, p.__dict__) ## отработал property и там метод set_old 



class MLModel:
    def __init__(self, name, accuracy=0.0):
        self._name = name
        self._accuracy = accuracy  # Protected
    
    @property
    def accuracy(self):
        # Геттер: вызывается при model.accuracy
        print("Получаю accuracy...")
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, value):
        # Сеттер: вызывается при model.accuracy = 0.95
        if 0 <= value <= 1:
            print("Устанавливаю accuracy...")
            self._accuracy = value
        else:
            raise ValueError("Accuracy должен быть от 0 до 1")
    
    @property
    def name(self):
        # Только чтение (нет сеттера)
        return self._name

# Использование
model = MLModel("LR-1", 0.85)

print(model.accuracy)  # Вызывает геттер: 0.85
model.accuracy = 0.95  # Вызывает сеттер
print(model.name)      # Только чтение
# model.name = "New"   # ❌ Ошибка! Нет сеттера