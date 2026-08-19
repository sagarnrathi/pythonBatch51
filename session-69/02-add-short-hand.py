class CPA_int:
    def __init__(self,init_n:int):
        if type(init_n) is not int:
            raise TypeError('init_n must be integer object')
        self.n = init_n


    def __add__(self,other):
        if type(other) is CPA_int:
            return CPA_int(self.n + other.n)
        elif type(other) is int:
            return CPA_int(self.n + other)
        else :
           raise TypeError('RHS object must be int or CPA_int')

    __radd__ = __add__

    def __iadd__(self,other):
        print('control flow  in cpa_int.__add__()')
        self.n = self.n + other.n
        return self

    def __str__(self):
        return str(self.n)

n1 = CPA_int(10)
n2 = CPA_int(5)

print(f'before n1 :{n1},n2:{n2} ')

n1 = n1+n2

print(f'after n1 :{n1},n2:{n2} ')


x = CPA_int(20)
y = CPA_int(5)

# x = x + y will work (as above)

print(f'BEFORE:x:{x}, y:{y}, id(x):{id(x)}')

x += y  # Internally converted to x = x + y 
        # x = x.__add__(y)
        # x = CPA_int.__add__(x, y)
print(f'AFTER:x:{x}, y:{y}, id(x):{id(x)}')