class CPA_int: 
    def __init__(self, init_n:int): 
        if type(init_n) is not int: 
            raise TypeError('Initializer must be a built-in int object')
        self.n = init_n 

    def __add__(self, other): 
        print('----Entered CPA_int.__add__()----')
        print(f'CPA_int.__add__():type(self):{type(self)}, type(other):{type(other)}')
        tmp = self.n + other.n 
        print(f'CPA_int.__add__():type(tmp):{type(tmp)}')
        result = CPA_int(tmp)
        print(f'CPA_int.__add__():type(result):{type(result)}')
        print(f'CPA_int.__add__():result.__dict__:{result.__dict__}')
        print(f'CPA_int.__add__():id(result):{id(result)}')
        print('----Leaving CPA_int.__add__()----')
        return result 
    
    def  __sub__(self,other):
        temp = self.n - other.n
        result = CPA_int(temp)
        return result


    def   __mul__(self,other):
        temp = self.n * other.n
        result = CPA_int(temp)
        return result

    def  __floordiv__(self,other):
        temp = self.n / other.n
        result = CPA_int(temp)
        return result

    def  __mod__ (self,other):
        temp = self.n % other.n
        result = CPA_int(temp)
        return result

    def  __truediv__ (self,other):
        return self.n / other.n
        

    def  __pow__(self,other):
        temp = self.n ** other.n
        result = CPA_int(temp)
        return result                    

    

    def __str__(self): 
        return str(self.n)


#-------------------CLIENT SIDE CODE---------------------# 

n1 = CPA_int(22)
n2 = CPA_int(5) 
print(f'type(n1):{type(n1)}, type(n2):{type(n2)}')

n3 = n1 + n2    

n4 = n1 - n2
n5 = n2 *n1

print(f'n1:{n1}, n2:{n2}, n3:{n3}, type(n3):{type(n3)}, id(n3):{id(n3)}')
print(f'n1:{n1}, n2:{n2}, n4:{n4}, type(n4):{type(n4)}, id(n4):{id(n4)}')
print(f'n1:{n1}, n2:{n2}, n5:{n5}, type(n5):{type(n5)}, id(n5):{id(n5)}')
'''
Expected result: Python should compute n1 + n2 and return an object of class CPA_int 
which internally contains an attribute 'n' attached to built-in integer whose value 
is the addition of that of values associated with attribute 'n' in objects n1 and n2. 

n3 = n1 + n2 

n1 + n2 Internally converted to n1.__add__(n2) which is in turn converted into 
CPA_int.__add__(n1, n2)
'''

print('Experiment only for addition operator')
r1 = n1.__add__(n2)
r2 = CPA_int.__add__(n1, n2)
print(f'n1:{n1}, n2:{n2}, r1:{r1}, type(r1):{type(r1)}, id(r1):{id(r1)}')
print(f'n1:{n1}, n2:{n2}, r2:{r2}, type(r2):{type(r2)}, id(r2):{id(r2)}')

'''
Subtraction: 
-   __sub__ 

Multiplication: 
*   __mul__ 

Integer division: (floor division)
//  __floordiv__ 

Modulus (remainder) 
%   __mod__ 

Floating point division: (true division)
/   __truediv__ 

Exponential" 
**  __pow__

'''