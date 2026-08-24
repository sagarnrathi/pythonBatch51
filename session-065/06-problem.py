class B1: 
    def f(self): 
        print('B1.f()')


class B2: 
    def f(self): 
        print('B2.f()')


class D(B1, B2): 
    pass 

objD = D() 
objD.f()