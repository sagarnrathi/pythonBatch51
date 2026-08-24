class cpa_str:
    def __init__(self,s:str):
        self.s = s

    def __mul__(self,n:int):
            if type(n) is not int:
                 raise TypeError
            if n<0:
                 raise ValueError
            print(f'type(self) : {type(self)}')
            print(f'type(self) : {type(self)}')

            s1 = self.s
            return_str = ''
            for i in range(n):
                 return_str = return_str + s1
            return return_str

    def __str__(self):
         return self.s
s = cpa_str('HAHA')
s1 = s*4
print('type(s1)',type(s1))
print('s1 :',s1)

