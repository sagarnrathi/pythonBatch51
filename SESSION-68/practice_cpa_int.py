class cpa_int:
    def __init__(self,init_n :int):
        if(type(init_n)!= int):
            raise TypeError("initilizer must be of built int type object")
        self.n = init_n

    def __add__(self,other):
        print('---- entered cpa_int.__add__()----')
        print(f'cpa_int.__add__():type(self):{type(self)},type(other):{type(other)}')
        tmp = self.n+other.n
        print(f'cpa_int.__add__():type(tmp):{type(tmp)}')
        result = cpa_int(tmp)
        print(f'cpa_int.__add__():type(result):{type(result)}')
        print(f'cpa_int.__add__():result.__dict__:{result.__dict__}')
        print(f'cpa_int.__add__():id(result):{id(result)}')
        print('---leaving cpa_int.__add__()----')
        return result

    def __sub__(self,other):
        return cpa_int(self.n - other.n)

    def __mul__(self,other):
        return cpa_int(self.n * other.n)

    def __floordiv__(self,other):
        return cpa_int(self.n//other.n)

    def __mod__(self,other):
        return cpa_int(self.n%other.n)

    def __neg__(self):
        return cpa_int(-self.n)

    def __pow__(self,other):
        return cpa_int(self.n**other.n)    

    def __truediv__(self, other):
        return self.n/other.n

    def __gt__(self,other):
        return self.n > other.n

    def __ge__(self,other):
        return self.n >= other.n

    def __lt__(self,other):
        return self.n<other.n

    def __le__(self,other):
        return self.n<=other.n

    def __eq__(self,other):
        return self.n == other.n

    def __ne__(self,other):
        return self.n != other.n

    def __and__(self,other):
        return cpa_int(self.n & other.n)

    def __or__(self,other):
        return  cpa_int(self.n | other.n)

    def __xor__(self,other):
        return cpa_int(self.n ^ other.n)

    def __invert__(self):
        return cpa_int(~self.n)

    def __lshift__(self,other):
        return cpa_int(self.n << other.n)

    def __rshift__(self,other):
        return cpa_int(self.n>>other.n)
    
    def __str__(self):
        return str(self.n)
n1 = cpa_int(22)
n2 = cpa_int(5)

print(f'type(n1):{type(n1)},type(n2):{type(n2)}')
n3 = n1+n2
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')
r1 = n1.__add__(n2)
print(r1)
r2 = cpa_int.__add__(n1,n2)
print(r2)


print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 - n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 * n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 // n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 % n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = -n1 
print(f'n1:{n1}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 ** n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 / n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

b = n1 > n2 
print(f'n1:{n1},n2:{n2}, n1 > n2:{b}')

b = n1 >= n2 
print(f'n1:{n1},n2:{n2}, n1 >= n2:{b}')

b = n1 < n2 
print(f'n1:{n1},n2:{n2}, n1 < n2:{b}')

b = n1 <= n2 
print(f'n1:{n1},n2:{n2}, n1 <= n2:{b}')

b = n1 == n2 
print(f'n1:{n1},n2:{n2}, n1 == n2:{b}')

b = n1 != n2 
print(f'n1:{n1},n2:{n2}, n1 != n2:{b}')



print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 & n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 | n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 ^ n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = ~n1 
print(f'n1:{n1}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 << n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')

print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')
n3 = n1 >> n2    
print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')
