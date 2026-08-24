class FunctionWrapper:
    def __init__(self,function_object):
        self.F = function_object

    def __call__(self,x,y,z):
        return self.F(x,y,z)

def compute(a,b,c):
    r1 = a + b
    r2 = b + c
    return r1 * r2

fw = FunctionWrapper(compute)
print('type(fw) :',type(fw))

result = fw(10,20,30)
print('result',result)
