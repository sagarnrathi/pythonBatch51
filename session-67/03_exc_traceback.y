import sys 

def f3(): 
    raise TypeError('Bad type : Artificially raised exception')

def f2(): 
    f3() 

def f1(): 
    f2() 


f1() 