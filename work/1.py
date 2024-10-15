class RationalFraction:
    def __init__(self, x, y):
        if y == 0:
            raise ValueError("Знаменатель не может быть равен 0")
        self.x = x
        self.y = y

    @staticmethod
    def commonDivider(t, h):
        while h != 0:
            t, h = h, t % h
        return t

    def printt(self):
        k = self.commonDivider(self.x, self.y)
        return f"{self.x // k}/{self.y // k}"

    def multiply1(self, other):
        xx = self.x * other.x
        yy = self.y * other.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def division1(self, other):
        if other.x == 0:
            raise ZeroDivisionError("Нельзя разделить на дробь, знаменатель которой равен 0")
        xx = self.x * other.y
        yy = self.y * other.x
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def addition1(self, other):
        if self.y == other.y:
            xx = self.x + other.x
            yy = self.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"
        else:
            xx = self.x * other.y + other.x * self.y
            yy = self.y * other.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"

    def subtraction1(self, other):
        if self.y == other.y:
            xx = self.x - other.x
            yy = self.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"
        else:
            xx = self.x * other.y - other.x * self.y
            yy = self.y * other.y
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"

    def multiply2(self, n):
        xx = self.x * n
        yy = self.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def divide2(self, n):
        xx = self.x
        yy = self.y * n
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def addition2(self, n):
        xx = self.x + n * self.y
        yy = self.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def subtraction2(self, n):
        xx = self.x - n * self.y
        yy = self.y
        k = self.commonDivider(xx, yy)
        return f"{xx // k}/{yy // k}"

    def power(self, n):
        if n >= 0:
            xx = self.x ** n
            yy = self.y ** n
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"
        else:
            xx = self.y ** (-n)
            yy = self.x ** (-n)
            k = self.commonDivider(xx, yy)
            return f"{xx // k}/{yy // k}"


a = RationalFraction(6, 8)
b = RationalFraction(3, 4)

print(f"Сокращение дроби 6/8: {a.printt()}")

print(f"Умножение 6/8 * 3/4: {a.multiply1(b)}")

print(f"Деление 6/8 / 3/4: {a.division1(b)}")

print(f"Сложение 6/8 + 3/4: {a.addition1(b)}")

print(f"Вычитание 6/8 - 3/4: {a.subtraction1(b)}")

print(f"Умножение 6/8 на 3: {a.multiply2(3)}")

print(f"Деление 6/8 на 2: {a.divide2(2)}")

print(f"Сложение 6/8 + 1: {a.addition2(1)}")

print(f"Вычитание 6/8 - 1: {a.subtraction2(1)}")

print(f"Возведение 6/8 в степень 2: {a.power(2)}")

print(f"Возведение 6/8 в степень -1: {a.power(-1)}")

c = RationalFraction(2, 3)
print(f"Возведение 2/3 в степень 0: {c.power(0)}")