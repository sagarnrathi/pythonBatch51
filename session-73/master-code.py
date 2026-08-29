import sys
EXIT_SUCCESS = 0
EXIT_FAILURE = -1

class usageError(Exception):
    pass

def main(argc : int,argv:[str]) -> None :
    if argc != 3 :
        raise usageError(f'bad Usage : correct usage :{argv[0]} src_path dest path')
    source_file_path,source_file_mode = argv[1],'r'
    destination_file_path,destination_file_mode = argv[2],'w'
    source_file_handle, destination_file_handle = None,None

    try :
        source_file_handle = open(source_file_path,source_file_mode)
        destination_file_handle = open(destination_file_path,destination_file_mode)

        for line in source_file_handle:
            print(line,file = destination_file_handle)

    except FileNotFoundError :
        print('bad path either for source or destination file')
        sys.exit(EXIT_FAILURE)
    except PermissionError:
        print('permission not granted to create a dest file or read source file')
    except :
        print("unanticipated error ")
        sys.exit(EXIT_FAILURE)
    finally :
        if source_file_handle is not None :
            source_file_handle.close()
        if destination_file_handle is not None:
            destination_file_handle.close()
    print('one file is copied successfully ')
    sys.exit(EXIT_SUCCESS)

main(len(sys.argv),sys.argv)

