class CPA_int:
    def __init__(self,init_n:int):
        if  type(init_n) is not int :
            raise TypeError('init_n must be an integer object')
        self.n = init_n

    def __add__(self,other):
        if(type(other) is CPA_int):
            print('CPA_int.__add__():both LHS and RHS are cpa_object')    
            return CPA_int(self.n+other.n)
        if(type(other) is int):
            print('CPA_int.__add__() : LHS is cpa int object and RHS is int object')
            tmp = self.n+other
            return CPA_int(tmp)
        else :
            raise TypeError('RHS object must be of CPA_int or int')

    def __radd__(self,other):
        if type(other) is not int:
            raise TypeError('LHS object must be int')        
        print('CPA_int.__radd__() :LHS is built in int object and rhs is CPA_INT')
        print(f'other : {id(other)}')
        return CPA_int(self.n+other);

    def __str__(self) -> str:
        return str(self.n)

n1 = CPA_int(300)
n2 = CPA_int(400)

n3 = n1 + n2
print(f'n1:{n1},n2:{n2},n3:{n3}')

n4 = n1+500
print(f'n1:{n1},n2:{n2},n4:{n4}')

n5 = 500 + n1
print(f'id : {id(500)}')
print(f'n1:{n1},n2:{n2},n5:{n5}')
