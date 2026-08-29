import sys,os
class  UsageError(Exception):
    pass
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
def main(argc:int,argv:[str])->None:
    if(argc != 2):
        raise UsageError(f'correct Usage :{argv[0]} text_file_path')
    file_desc = os.open(argv[1],os.O_RDONLY)
    if(file_desc < 0):
        print(f'{argv[1]} could not be opened ')
        sys.exit(EXIT_FAILURE)
    BUFFER_SIZE = 4096
    STDOUT_DESCRIPTOR  = 1

    while True :
        read_buffer = os.read(file_desc,BUFFER_SIZE)
        if(len(read_buffer) == 0):
            break;
        os.write(STDOUT_DESCRIPTOR,read_buffer)
    os.close(file_desc)

    sys.exit(EXIT_SUCCESS)
main(len(sys.argv),sys.argv)


