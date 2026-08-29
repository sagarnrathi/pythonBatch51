import sys

file_name = 'pqr.txt'
mode = 'w'

try:
    f_handle = open(file_name,mode)
    print('This is first line in file ',file=f_handle)
    L = [True,10,1.1,'Hello']
    for x in L:
        print(x,file=f_handle)
    print('This is last line in file',file = f_handle)
except FileNotFoundError :
    print('Invalid file name or path',file_name)
    sys.exit(-1)
except PermissionError:
    print('permission denied to create  a file ',file_name)
except :
    print('file could not be opned because of unexpcted reason')
    sys.exit(-1)
finally:
    f_handle.close()

mode = 'r'

try :
    f_handle = open(file_name,mode)
    for line in f_handle:
        print(line,end='')
except FileNotFoundError:
    print('Invalid file name or path',file_name)
    sys.exit(-1)
except PermissionError :
    print('permission denied to access the file ',file_name)
    sys.exit(-1)
except:
    print('file could not be open in read mode unexpcted error')
    sys.exit(-1)
finally:
    f_handle.close()