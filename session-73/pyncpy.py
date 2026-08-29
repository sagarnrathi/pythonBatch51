import sys
EXIT_SUCCESS = 0
EXIT_FAILURE = -1

class UsageError(Exception):
    pass

def main(argc:int,argv:[str]) -> None:
    if argc < 3:
        raise UsageError(f'correct usage : {argv[0]} src-1 ...src-n dest')
    destination_file_name,destination_file_mode = argv[-1],'w'
    destination_file_handle = None

    try :
        destination_file_handle = open(destination_file_name,destination_file_mode)
    except FileNotFoundError :
        print(f'{destination_file_name} is invalid path')
        sys.exit(EXIT_FAILURE)
    except PermissionError :
        print(f'{destination_file_name} permission denied to create ')
        sys.exit(EXIT_FAILURE)
    except :
        print("something went wrong while openig dest file")
        sys.exit(EXIT_FAILURE)
    for source_file_path in argv[1:argv-1] :
        

