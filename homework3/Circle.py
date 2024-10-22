import math

class Circle:
    def __init__(self, new_center_x, center_y, radius):
        self.center_x = new_center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area_2(self, other):
        d = math.sqrt((self.center_x - other.center_x) ** 2 + (self.center_y - other.center_y) ** 2)
        if d >= self.radius + other.radius:
            return 0  
        if d <= abs(self.radius - other.radius):
            return math.pi * min(self.radius, other.radius) ** 2  
        
        r1, r2 = self.radius, other.radius
        part1 = r1 ** 2 * math.acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1))
        part2 = r2 ** 2 * math.acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2))
        part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
        return part1 + part2 - part3
        
circ1 = Circle(1, 1, 8)  
circ2 = Circle(6, 4, 9) 

print(f"Площадь circ1: {circ1.area()}")  
print(f"Площадь circ2: {circ2.area()}")  
print(f"Длина circ1: {circ1.perimeter()}")  
print(f"Длина circ2: {circ2.perimeter()}")  
print(f"Площадь пересечения: {circ1.area_2(circ2)}")  