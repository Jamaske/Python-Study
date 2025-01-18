class Expression:
    def __init__(self, value, history=None, priority = 5):
        self.value = value
        self.priority = priority
        self.history = history if history is not None else [str(value)]

    def _binary(self, operation, priority, other, result):
        M = max(len(self.history), len(other.history))
        m = min(len(self.history), len(other.history))
        history = [None] * (1 + M)
        history[0] = str(result)
        #binary operation upon prepared values does not need them wraped in brackets
        history[1] = f"{self.history[0]} {operation} {other.history[0]}"
        w1 = '(' if self.priority < priority else ''
        w2 = ')' if self.priority < priority else ''
        w3 = '(' if other.priority <= priority else ''
        w4 = ')' if other.priority <= priority else ''
        for i in range(1,m):
            history[i + 1] = f"{w1}{self.history[i]}{w2} {operation} {w3}{other.history[i]}{w4}"
        for i in range(len(self.history), M):#other hist longer
            history[i + 1] = f"{w1}{self.history[-1]}{w2} {operation} {w3}{other.history[i]}{w4}"
        for i in range(len(other.history), M):#self hist longer
            history[i + 1] = f"{w1}{self.history[i]}{w2} {operation} {w3}{other.history[-1]}{w4}"
        return Expression(result, history=history, priority=priority)
    
    def _unary(self, safix, postfix, priority, result):
        history = [None] * (len(self.history) + 1)
        history[0] = str(result)
        w1 = '(' if self.priority < priority else ''
        w2 = ')' if self.priority < priority else ''
        for i in range(len(self.history)):
            history[i+1] = f"{safix}{w1}{self.history[i]}{w2}{postfix}"
        return Expression(result, history=history, priority=priority)


    def flush(self):
        del self.history[1:]
        self.priority = 5


    def __add__(self, other):
        if not isinstance(other, Expression): other = Expression(other)
        result = self.value + other.value
        return self._binary("+", 1, other, result)

    def __sub__(self, other):
        if not isinstance(other, Expression): other = Expression(other)
        result = self.value - other.value
        return self._binary("-", 1, other, result)

    def __neg__(self):#dont like negation takeing step in expresions mutations
        result =  -self.value
        priority = 4
        history = [None] * len(self.history)
        history[0] = str(result)
        w1 = '(' if self.priority < priority else ''
        w2 = ')' if self.priority < priority else ''
        for i in range(1,len(self.history)):
            history[i] = f"-{w1}{self.history[i]}{w2}"
        return Expression(result, history=history, priority=priority)

    def __mul__(self, other):
        if not isinstance(other, Expression): other = Expression(other)
        result = self.value * other.value
        return self._binary("*", 2, other, result)

    def __truediv__(self, other):
        if not isinstance(other, Expression): other = Expression(other)
        if other.value == 0: raise ZeroDivisionError("Division by zero is undefined.")
        result = self.value / other.value
        return self._binary("/", 2,other, result)
    
    def __abs__(self):
        result = abs(self.value)
        return self._unary("|", "|", 4, result)

    def __pow__(self, other):
        if not isinstance(other, Expression): other = Expression(other)
        result = self.value ** other.value
        return self._binary("^", 3,other, result)

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)): other = type(self)(other)
        return self.value == other.value

    def __lt__(self, other) -> bool:
        if not isinstance(other, type(self)): other = type(self)(other)
        return self.value < other.value

    def __gt__(self, other) -> bool:
        if not isinstance(other, type(self)): other = type(self)(other)
        return self.value > other.value

    def steps(self):
        return " = ".join(self.history[::-1])

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return self.history[0]

    def __repr__(self):
        return self.history[0]


if __name__ == "__main__":
    # Example Usage
    x = Expression(4)
    y = Expression(2)
    z = Expression(5)
    w = Expression(3)
    a = Expression(7)
    b = Expression(3)
    #exp = (x - y) * z / (w ** (a - b))
    exp = x*-5 + 3 + 2 + 150
    print("Final result:", exp)
    print("Steps:")
    print(exp.steps())
