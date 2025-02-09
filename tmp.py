
def foo(number, string):
    for i in range(number):
        print(string)

class car:
    def __init__(self, long, stearing_wheel):
        if long:
            self.numberofWheels = 6
        else:
            self.numberofWheels = 4
        self.stearing_wheel = stearing_wheel
    
    def drive(self):
        self.numberofWheels -= 1
        print("wheel fall off")
        if self.stearing_wheel == "left":
            print("actualy you died")
        if self.numberofWheels == 4:
            print("you piked up some bitches")
MyCar = car(False, "left")
Yourcar = car(True, "right")

print("my car")
MyCar.drive()

print("your car")
Yourcar.drive()
Yourcar.drive()



'''
class FUCK:
    field = "fuck"


    def method(x, n = 1):
        for ㅤ in range(n):
            print(x.field)

fuck = FUCK()

fuck.method()




FUCK.method2 = lambda x: print("Fuck method2")

fuck.method2()
'''