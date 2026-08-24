
class B1: 
    def f1(self): 
        print('In B1.f1()')

    def f2(self): 
        print('In B1.f2()')


class B2: 
    def g1(self): 
        print('In B2.g1()')

    def g2(self): 
        print('In B2.g2()')

# This is an example of multiple-inheritance 
class D(B1, B2): 
    def h1(self): 
        print('In D.h1()')

    def h2(self): 
        print('In D.h2()')


objD = D() 

objD.h1()   # Resolved to D.h1()
objD.h2()   # Resolved to D.h2() 

objD.g1()   # Resolved to B2.g1() 
objD.g2()   # Resolved to B2.g2() 

objD.f1()   # Resolved to B1.f1()
objD.f2()   # Resolved to B1.f2()