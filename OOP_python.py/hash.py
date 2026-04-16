# hash("Python") -> -2824395756...
# hash(123) -> 123
#hash((1,2,3)) -> 5293440672....

#print(hash("python"))
#print(hash((1,2,3)))

# еслси попробуем hash([1,2,3,]) -> будет ошибка, так как list - это измен. объект 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1,2)
p2 = Point(1,2) # будет один ключь из-за __hash__

# если не использовать hash, тогда ключи будут разными  

print(hash(p1), hash(p2), sep= "\n")
print(p1 == p2)

d = {}
d[p1] = 1
d[p2] = 2
print(d)