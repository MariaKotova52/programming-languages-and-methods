class  RationalFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен 0")
        self.numerator = numerator
        self.denominator = denominator

    def nod(a, b):
        a1 = max(abs(a), abs(b))
        b1 = min(abs(a), abs(b))
        while b1 != 0:
            a1, b1 = b1, a1 % b1
        if a <= 0 and b <= 0:
            return -a1
        return a1

    def correct_minus(a, b):
        if a >= 0 and b < 0:
            b *= -1
            a *= -1
        return a, b

    def addition(self, other):
        if isinstance(other, RationalFraction):
            if self.denominator == other.denominator:
                res_numerator = self.numerator + other.numerator
                res_denominator = self.denominator
            else:
                res_numerator = (
                    self.numerator * other.denominator
                    + other.numerator * self.denominator
                )
                res_denominator = self.denominator * other.denominator
        else:
            res_numerator = self.numerator + other * self.denominator
            res_denominator = self.denominator
        k = RationalFraction.nod(res_numerator, res_denominator)
        res_numerator, res_denominator = RationalFraction.correct_minus(
            res_numerator, res_denominator
        )
        return f"{res_numerator // k}/{res_denominator // k}"

    def subtraction(self, other):
        if isinstance(other, RationalFraction):
            if self.denominator == other.denominator:
                res_numerator = self.numerator - other.numerator
                res_denominator = self.denominator
            else:
                res_numerator = (
                    self.numerator * other.denominator
                    - other.numerator * self.denominator
                )
                res_denominator = self.denominator * other.denominator
        else:
            res_numerator = self.numerator - other * self.denominator
            res_denominator = self.denominator
        k = RationalFraction.nod(res_numerator, res_denominator)
        res_numerator, res_denominator = RationalFraction.correct_minus(
            res_numerator, res_denominator
        )
        return f"{res_numerator // k}/{res_denominator // k}"

    def multiply(self, other):
        if isinstance(other, RationalFraction):
            res_numerator = self.numerator * other.numerator
            res_denominator = self.denominator * other.denominator
        else:
            res_numerator = self.numerator * other
            res_denominator = self.denominator
        k = RationalFraction.nod(res_numerator, res_denominator)
        res_numerator, res_denominator = RationalFraction.correct_minus(
            res_numerator, res_denominator
        )
        return f"{res_numerator // k}/{res_denominator // k}"

    def division(self, other):
        if isinstance(other, RationalFraction):
            if other.numerator == 0:
                raise ZeroDivisionError(
                    "Нельзя разделить на дробь, числитель которой равен 0"
                )
            res_numerator = self.numerator * other.denominator
            res_denominator = self.denominator * other.numerator
        else:
            if other == 0:
                raise ZeroDivisionError("Нельзя делить на 0")
            res_numerator = self.numerator
            res_denominator = self.denominator * other
        k = RationalFraction.nod(res_numerator, res_denominator)
        res_numerator, res_denominator = RationalFraction.correct_minus(
            res_numerator, res_denominator
        )
        return f"{res_numerator // k}/{res_denominator // k}"

    def power(self, n):
        k = RationalFraction.nod(self.numerator, self.denominator)
        self.denominator //= k
        self.numerator //= k
        if n >= 0:
            res_numerator = self.numerator**n
            res_denominator = self.denominator**n
        else:
            res_numerator = self.denominator ** (-n)
            res_denominator = self.numerator ** (-n)
        res_numerator, res_denominator = RationalFraction.correct_minus(
            res_numerator, res_denominator
        )
        return f"{res_numerator}/{res_denominator}"
