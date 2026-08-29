import os,sys
'''
s =  input('Enter a string : ')

byte_str = s.encode()
os.write(1,byte_str)
'''
def cpa_print(*args,sep=' ',end='\n',file=sys.stdout,flush=False):
    master_str = ''
    for each in args:
        master_str = master_str + each + sep
    master_str = master_str+end
    #master_str = master_str.encode()
    file.write(master_str)

cpa_print("sagar","rathi")

    
    
