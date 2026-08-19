class Quadrilateral:

    def __init__(self,s1,s2,s3,s4):
        self.s1,self.s2,self.s3,self.s4 = s1,s2,s3,s4

    def area(self) -> float:
        s = (self.s1 + self.s2 + self.s3+self.s4)/2
        return (s-self.s1)*(s-self.s2)*(s-self.s3)*(s-self.s4) ** 0.5

class square:
    def __init__(self,s):
        Quadrilateral.__init__(self,s,s,s,s)    
        self.s = s
    def area(self):
        return self.s **2
    
