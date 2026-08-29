def generic_exception_handler(should=False,want_tb=False):
    from sys import exc_info,exit
    from traceback import print_tb

    exc_name,exc_data,exc_tb = exc_info()
    print(exc_name.__name__,exc_data,sep=':')

    if want_tb:
        print_tb(exc_tb)

    if should:
        exit()

src_file_path = input('enter source file path : ')
trg_file_path = input('enter Target file path : ')

try :
    src_handle = open(src_file_path,'r')
    dest_handle = open(trg_file_path,'w')

    for line in src_handle:
        print(line,end='',file=dest_handle)
except :
    generic_exception_handler()

finally :
    src_handle.close()
    dest_handle.close()

    