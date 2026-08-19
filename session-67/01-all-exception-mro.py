for name in dir(__builtins__):
    if name.endswith('Error') or name.endswith('warning') or name in ['BaseException','Exception']:
        exception_class = __builtins__.dict[name]
        print('exception name :',name)
        print('\t',exception_class.__mro__)
