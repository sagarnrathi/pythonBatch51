import sys
import traceback    

def f3():
    raise TypeError('Bad type : Artificially raised exception')
def f2():
    f3()
def f1():
    f2()

try :
    f1()
except:
    exc_name,exc_data,exc_tb = sys.exc_info()
    print('exc name :',exc_name)
    print('exc_data : ',exc_data)
    print('type(exc_tb) :',type(exc_tb))
    print("programatically printing traceback info")
    traceback.print_tb(exc_tb)

