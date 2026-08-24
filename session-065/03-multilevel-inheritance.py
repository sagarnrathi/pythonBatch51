class B:
    def f1(self):
        print('In B F1()')
    def f2(self):
        print('In B f2()')
    def f3(self):
        print('In B f3()')

class D(B):
    def f2(self): 
        B.f2(self)
        print('In D.f2()')

    # f3() is a replacor 
    def f3(self): 
        print('In D.f3()')

    def g1(self): 
        print('In D.g1()')

    def g2(self): 
        print('In D.g2()')

class D1(D): 
    def f3(self): 
        print('In D1.f3()')

    def h1(self): 
        print('In D1.h1()')

    def h2(self): 
        print('In D1.h2()')
objD1 = D1() 

objD1.h1()  # h1() is a derived specific method of class D1 
objD1.h2()  # h2() is a derived specific method of class D1 
objD1.f3()  # B.f3() is overridden by D.f3() which in turn is overridden by 
            # D1.f3(). According to look up rules call objD1.f3() will be 
            # resolved to D1.f3()

objD1.f2()  # B.f2() is overridden by D.f2() which is not overridden by D1
            # Therefore call to f2() on object of D1 will be resolved to 
            # D.f2() but because D.f2() also calls B.f2() inside it 
            # B.f2() will also be executed 

objD1.g1()  # g1() is an inheritor here. There is not D1.g1() but there is a 
            # D.g1() and therefore, call to objD1.g1() will be resolved to D.g1() 


objD1.g2()  # g2() is an inheritor here. There is not D1.g2() but there is a 
            # D.g2() and therefore, call to objD1.g2() will be resolved to D.g2() 

objD1.f1()  # B.f1() is present neither overridden by D or D1 
            # therefore call to objD1.f1() will be resolved to B.f1() 