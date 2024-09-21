class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        x = self.length * 2
        y = self.width * 2
        return x + y
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)