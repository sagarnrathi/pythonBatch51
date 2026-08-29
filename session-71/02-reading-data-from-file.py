f_handle = open('abc.txt','r')
print('type(f_handle)',type(f_handle))
print('f_handle.fileno():',f_handle.fileno())

for line in f_handle:
    print(line,end='')

f_handle.close()