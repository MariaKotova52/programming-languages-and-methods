class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  
        self.y1 = y1
        self.x2 = x2 
        self.y2 = y2

    def area(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)

    def perimeter(self):
        return 2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1))

    def area_2(self, other):
        x_overlap = max(0, min(self.x2, other.x2) - max(self.x1, other.x1))
        y_overlap = max(0, min(self.y2, other.y2) - max(self.y1, other.y1))
        return x_overlap * y_overlap




rect1 = Rectangle(1, 1, 8, 5)  
rect2 = Rectangle(6, 4, 9, 7)  

print(f"Площадь rect1: {rect1.area()}")  
print(f"Площадь rect2: {rect2.area()}")  
print(f"Периметр rect1: {rect1.perimeter()}")  
print(f"Периметр rect2: {rect2.perimeter()}")  
print(f"Площадь пересечения: {rect1.area_2(rect2)}")  


