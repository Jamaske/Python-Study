class A:
    """my doc"""
    def __init__(self, id_):
        pass
        #self.id = id_

    def __hash__(self):
        return 1


d = {A(1): 1}
d[A(2)] = 2
d[A(1)] = 3
it = d.items()
for k, v in it:
    print(k, v)




def g():
    x = 5
    def f():
        print(x)

    return f
x = 3
g()()
