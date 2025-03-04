def Template(digits):
    class FixPoint:
        
        def __init__(self, value):
            self.mantisa = int(value * self.shift)

        @classmethod
        def mantisaConstructor(cls, mantisa):
            instance = cls.__new__(cls)
            instance.mantisa = mantisa
            return instance

        def __float__(self) -> float:
            return self.mantisa / self.shift

        def __eq__(self, other) -> bool:
            if not isinstance(other, type(self)): other = type(self)(other)
            return self.mantisa == other.mantisa

        def __lt__(self, other) -> bool:
            if not isinstance(other, type(self)): other = type(self)(other)
            return self.mantisa < other.mantisa

        def __gt__(self, other) -> bool:
            if not isinstance(other, type(self)): other = type(self)(other)
            return self.mantisa > other.mantisa

        def __add__(self, other):
            if not isinstance(other, type(self)):
                other = type(self)(other)
            return self.mantisaConstructor(self.mantisa + other.mantisa)

        def __sub__(self, other):
            if not isinstance(other, type(self)):
                other = type(self)(other)
            return self.mantisaConstructor(self.mantisa - other.mantisa)
        
        def __neg__(self):
            return self.mantisaConstructor(- self.mantisa)

        def __mul__(self, other):
            if not isinstance(other, type(self)):
                other = type(self)(other)
            return self.mantisaConstructor(int(self.mantisa * other.mantisa / self.shift))

        def __truediv__(self, other):
            if not isinstance(other, type(self)):
                other = type(self)(other)
            if other.mantisa == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return self.mantisaConstructor(int(self.mantisa * self.shift / other.mantisa))

        def __abs__(self):
            return self.mantisaConstructor(abs(self.mantisa))

        def __str__(self):
            return f"{self.__float__():>{4 + self.digits}.{self.digits}f}"

    FixPoint.digits = digits #add static class fied that parametrize it (tamplate<int digits>)
    FixPoint.shift = 10 ** digits
    return FixPoint


if __name__ == "__main__":
    FP2 = Template(2)
    
    # Example usage
    pm1 = FP2(1)
    pm2 = FP2(2.6799)

    result_add = pm1 + pm2
    result_sub = pm1 - pm2
    result_mul = pm1 * pm2
    result_div = (pm1 / 3) * 3

    print("Addition:", result_add)
    print("Subtraction:", result_sub)
    print("Multiplication:", result_mul)
    print("Division:", result_div)