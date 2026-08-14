def exception_raiser_function(n:int):

    if(type(n) is not int):
        raise TypeError('n must be integer')
    if(n <1):
        raise ValueError('n must be positive integer')
    if(n ==1) :
        raise NameError("artificially raisein name erro")
    else :
        raise ArithmeticError('artificially rasing attribute error ')

try :
    exception_raiser_function(1.1)
except TypeError:
    print('syntax 1 : typeerror occured ')

try :
    exception_raiser_function(5)
except:
    print('syntax 5 : some exception occured')

try :
    exception_raiser_function(-4)
except ValueError as e :
    print('syntax 2 :',e)

try :
   exception_raiser_function(int(input('enter an ineger :'))) 
except(ValueError,AttributeError,NameError) :
    print('one of the following exception occured ValueError,AttributeError,NameError')
except TypeError as e:
    print(e)
except :
    print('some unknown error ')

