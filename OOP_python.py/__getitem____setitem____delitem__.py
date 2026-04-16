class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, key):
        if 0<= key <= len(self.marks):
            return self.marks[key]
        else:
            raise IndexError("неверный индекс")
    
    def __setitem__(self, key, value):
        if not isinstance(key,int):
            raise TypeError("индекс должен быть неотрицательным")
        
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key] 
        

s1 = Student("сергейй", [1,4,5,3,5,4,3])
s1[10] = 4
del s1[2]
print(s1.marks)