

class quaternion:
    # def __init__():
    #     self.w:int = 2
    #     self.x:int = 0
    #     self.y:int = 0
    #     self.z:int = 0

    def __init__(self,w, x, y, z):
        self.w:int = w
        self.x:int = x
        self.y:int = y
        self.z:int = z
    


    def __mul__ (self, q2:'quaternion')->'quaternion':
        q = quaternion(
            self.w * q2.w - self.x * q2.x - self.y * q2.y - self.z * q2.z,
            self.w * q2.x + self.x * q2.w + self.y * q2.z - self.z * q2.y,
            self.w * q2.y - self.x * q2.z + self.y * q2.w + self.z * q2.x,
            self.w * q2.z + self.x * q2.y - self.y * q2.x + self.z * q2.w,
        )
        if q.w<0: q = -q
        return q

    # def __rmul__ (self, q1:'quaternion')->'quaternion':
    #     return quaternion(
    #         q1.w * self.w - q1.x * self.x - q1.y * self.y - q1.z * self.z,
    #         q1.w * self.x + q1.x * self.w + q1.y * self.z - q1.z * self.y,
    #         q1.w * self.y - q1.x * self.z + q1.y * self.w + q1.z * self.x,
    #         q1.w * self.z + q1.x * self.y - q1.y * self.x + q1.z * self.w,
    #     )
    
    def __imul__ (self, q2:'quaternion')->'quaternion':
        self.w, self.x, self.y, self.z = (
            self.w * q2.w - self.x * q2.x - self.y * q2.y - self.z * q2.z,
            self.w * q2.x + self.x * q2.w + self.y * q2.z - self.z * q2.y,
            self.w * q2.y - self.x * q2.z + self.y * q2.w + self.z * q2.x,
            self.w * q2.z + self.x * q2.y - self.y * q2.x + self.z * q2.w,
        )
    

    def __ifloordiv__ (self, scalar:int)->'quaternion':
        self.w, self.x, self.y, self.z = self.w // scalar, self.x // scalar, self.y // scalar, self.z // scalar
        return self

    def __idiv__ (self, scalar)->'quaternion':
        self.w, self.x, self.y, self.z = self.w / scalar, self.x / scalar, self.y / scalar, self.z / scalar
        return self

    def __neg__(self)->'quaternion':
        return quaternion(-self.w, -self.x, -self.y, -self.z)

    def __invert__(self)->'quaternion':
        """get conjugate quaternion"""
        return quaternion(self.w, -self.x, -self.y, -self.z)
    
    def __str__(self):
        return f'({self.w} + {self.x}i + {self.y}j + {self.z}k)'

class orientation:

    def __init__ (self):
        self.quaternion = quaternion(1,0,0,0)
        self.sqrt2pow = False
        
        print(str(self))

    def rotate(self,x, y, z):
        """
        rotate by 90 degrese oround given vector.
        vector should be normalized
        """
        flag = self.flag()

        self.quaternion = quaternion(1, x, y, z) * self.quaternion

        flag = flag and self.flag()

        if (not self.sqrt2pow and flag) or (self.sqrt2pow and not flag):
            self.quaternion //= 2
        self.sqrt2pow = not self.sqrt2pow

    def flag(self):return bool(self.quaternion.x) or bool(self.quaternion.y) or bool(self.quaternion.z)

    def __str__(self):
        return f'orientation is:\n(1/2)^{int(self.flag())}*(sqrt2)^{int(self.sqrt2pow)} * {str(self.quaternion)}\n'

    def orientateVector(self,x, y, z):
        """
        take vector coordinates in rotated coordinate sysetem
        return vector coordiantes in absolute coordiantae system
        rotate vector by curent orientation
        """

        V = self.quaternion * quaternion(0,x,y,z) * ~self.quaternion
        V //= (1 << 2*self.flag() - self.sqrt2pow)
        return V
        

ort = orientation()
vector = (1,2,3)

ort.rotate(1,0,0)
print(str(ort))
ort.rotate(1,0,0)
print(str(ort))
ort.rotate(1,0,0)
print(str(ort))
ort.rotate(1,0,0)
print(str(ort))
# ort.rotate(0,0,1)
# print(str(ort))


vector2 = ort.orientateVector(*vector)
print(vector2)
