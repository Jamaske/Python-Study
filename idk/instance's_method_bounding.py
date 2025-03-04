class A:
    def f(self):
        pass

print(A.f)

a = A()
id_ = id(a)
#just formated print of id
print(f"{0:44}x{id_ :016X}")
print(a.f)

import types
a_f = types.MethodType(A.f, a)
print(a_f)

print(A.f.__get__(a))