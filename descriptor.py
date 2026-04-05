class integer:
    
    @classmethod
    def verify_coords(cls, coord):
        if type(coord) != int:
            raise TypeError("координата не должна быть целым числом")
    
    def __set_name__(self,owner,name):
        self.name = "_" + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        print(f"сработал сеттер из класса integer {self.name} = {value}")
        self.verify_coords(value)
        instance.__dict__[self.name] = value


class point3D:
    x = integer()
    y = integer()
    z = integer()

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z


    # было оч громоздко 
    # @property
    # def x(self):
    #     return self._x
    
    # @x.setter
    # def x(self,coord):
    #     self.verify_coords(coord)
    #     self._x = coord

    # @property
    # def y(self):
    #     return self._y
    
    # @y.setter
    # def y(self,coord):
    #     self.verify_coords(coord)
    #     self._y = coord

    # @property
    # def z(self):
    #     return self._z
    
    # @z.setter
    # def z(self,coord):
    #     print("абвгд")
    #     self.verify_coords(coord)
    #     self._z = coord

U = point3D(1,2,3)
print(U.__dict__, U.x)

