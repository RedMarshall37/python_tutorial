from cmath import inf


class Parallelepiped:
    def info(cls):
        return dir(cls)

    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
    
    def volume(self):
        return self.width*self.length*self.height
    
    def square_base(self):
        return self.width*self.length
 
    def square_sides(self):
        return 2 * (self.width*self.height + self.length*self.height) 

    

p = Parallelepiped(1,2,3)
print(f"p.info() = {p.info()}")
print(f"p.volume() = {p.volume()}")
print(f"p.square_base() = {p.square_base()}")
print(f"p.square_sides() = {p.square_sides()}")