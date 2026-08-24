class cpa_int:
    def __init__(self,n:int):
        if type(n) is not int:
            raise TypeError(f'n must be int provided {type(n).__name__}')
        self.n = n

    def __add__(self,other):
        if type(other) is  int:
            return cpa_int(self.n +other.n)
        elif type(other) is cpa_int:
            return cpa_int(self.n + other.n)
        else :
            raise TypeError(f'rhs operant must be cpa_int or int,provided :{type(other).__name__}')

    __radd__ = __add__
    def __iadd__(self, other):
         self.n = self.n + other.n
         return self
    def __str__(self):
        return str(self.n)

    __rstr__ = __str__
    

a = cpa_int(5)
b = cpa_int(6)
a+=b
print(a)
print(a+b)
