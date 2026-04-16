from abc import ABC, abstractmethod
import csv

class MLModel(ABC):

    total_models = 0

    def __init__(self,name,model_type):
        self.name = name
        self.model_type = model_type
        self._accuracy = 0.0
        self._is_trained = False
        MLModel.total_models += 1

    @property
    def accuracy(self):
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self,value):
        if (0 <= value <= 1):
            self._accuracy = value
        else :
            raise ValueError("accuracity должна быфть в пределах от 0 до 1")

    @classmethod
    def get_total_models(cls):
        return cls.total_models   

    @abstractmethod
    def train(self,data):
        pass

    @abstractmethod
    def predict(self,x):
        pass
    
    def __str__(self):
        # Возвращает ЧИТАЕМУЮ строку
        status = "Обучена" if self._is_trained else "Не обучена"
        return f"{self.name} ({self.model_type}): {status}"


class Lineral_Regression(MLModel):
    def __init__(self, name,lr = 0.01):
        super().__init__(name,'LiLineral_Regression')
        self.lr = lr
        self.coef = 0.0
        self.accuracy = 0.2
    
    def train(self,data):
        self.coef = sum(data) / len(data) if data else 0 
        self._is_trained = True
        self.accuracy = 0.7
        print(f"модель {self.name} обучена и готова")

    def predict(self,x):
        return x * self.coef
    
class Descision_Tree(MLModel):
    def __init__(self, name, max_depth = 5):
        super().__init__(name,'Descision_Tree')
        self.max_depth = max_depth
        self.tree_data = None
        self.accuracy = 0.3
    
    def train(self,data): 
        self._is_trained = True
        self.tree_data = sum(data) / len(data) if data else 0
        self.accuracy = 0.8
        print(f"модель {self.name} обучена и готова")

    def predict(self,x):
        return self.tree_data if self.tree_data else 0
    
# task 4
def Model_save_log(name, filename):
    with  open(filename, "a", encoding="utf-8",newline='') as f:
       writer = csv.DictWriter(f, fieldnames = ['name', 'accuracy', 'status']) 
       writer.writeheader()
       data = [{'name' : name.name,
                'accuracy': name.accuracy,
                'status': name._is_trained}]
       
       writer.writerows(data)

def Load_model_logs(filename):
    logs = []
    with open(filename,"r" ,encoding="utf-8",newline='\n') as f:
        reader = csv.DictReader(f)
        for row in reader:  # ← Читаем каждую строку!
            logs.append(row)
    return logs

def save_predictions(name,filename,data):
    import os
    
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        new = csv.DictWriter(f, fieldnames=['Model Name','input', 'prediction'])
        
        if file_exists and os.path.getsize(filename) > 0:
            f.write('\n')

        if not file_exists:
            new.writeheader()

        for x in data:
            new.writerow({
                'Model Name': name.name,
                'input': x,
                'prediction': name.predict(x)  # ← Предсказание для каждого x
            })



print(f"Всего моделей: {MLModel.get_total_models()}")

lr = Lineral_Regression("Lineral" , lr=0.01)
Dt = Descision_Tree("Decision", max_depth=10)

print(f"Всего моделей: {MLModel.get_total_models()}") 

####### реализация для __str__ ########
lr1 = Lineral_Regression("LR-1")

Model_save_log(lr1,"Lineral Regression")
logs = Load_model_logs("Lineral Regression")
print(logs)

lr1.train([1,3,4,5,76,899,4,23,1,2])
save_predictions(lr1,"predictions" ,[10,20,30])
 

Model_save_log(Dt,"Descision Tree")
logs = Load_model_logs("Descision Tree")
print(logs)

Dt.train([1,3,4,5,76,899,4,23,1,2])
save_predictions(Dt,"predictions" ,[15,25,35])

#######################################

lr.train([1, 2, 3, 4, 5])

print(lr.__dict__)  
print(Dt.__dict__)

print(f"Accuracy LR: {lr.accuracy}")  # 0.0
lr.accuracy = 0.95  # ✅ Работает
# lr.accuracy = 1.5  # ❌ ValueError!
print(f"Accuracy LR: {lr.accuracy}")

print(f"Предсказание LR(10): {lr.predict(10)}")
print(f"Предсказание DT(10): {Dt.predict(10)}")


