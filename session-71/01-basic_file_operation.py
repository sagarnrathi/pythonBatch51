f_handle = open('abc.txt','w')

print('type(f_handle)',type(f_handle))
print('this is first line in a file ',file=f_handle)

L = [True,10,1.1,'CoreCode']

for x in L:
    print(x,type(x),file=f_handle)

print('This is last line in file ',file=f_handle)
f_handle.close()