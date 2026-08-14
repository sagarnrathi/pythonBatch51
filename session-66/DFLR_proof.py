class B1:
    def f1(self):
        print('B1.f1()')

class B2 :
    def f1(self):
        print('B2.f1')

class B3 :
    def f1(self):
        print('B3.f1()')


class B4 :
    def f(self):
        print('B4.f1()')


class D1(B1,B2):
    def f1(self):
        print('D1.f1()')

class D2(B3,B4):
    def f1(self):
        print('D2.f1()')

class D(D1,D2):
    def f1(self):
        print('d.f1()');

objD = D()
print(D.__mro__)
        