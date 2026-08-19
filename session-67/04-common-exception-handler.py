def generic_exception_handler(should_exit=False,Require_tb = False):
        from sys import exc_info
        exc_name,exc_data,exc_tb = exc_info()
        if Require_tb :
                from traceback import print_tb
                print(exc_tb)
        if should_exit:
                from sys import exit
                exit()
                
    