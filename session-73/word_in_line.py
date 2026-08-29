def get_word_count(s:str)->int :
    if(type(s)) is not str:
        raise TypeError('input must be string object')

    IN,OUT = 1,2
    state = OUT
    word_count = 0

    for c in s:
        if state is OUT and not c.isspace():
            state = IN
            word_count+=1
        elif state is IN and c.isspace():
            state = OUT
    return word_count

s1 = 'core code programming academy '
s2 = '  \n\n foobar \n\n bar \n\n hahahaha'

print(f'words in {s1}:{get_word_count(s1)}')
print(f'words in {s2} : {get_word_count(s2)}')

