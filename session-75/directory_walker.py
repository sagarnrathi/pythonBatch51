import os,sys

class UsageError(Exception):
    pass

EXIT_SUCCESS = 0;
EXIT_FAILURE = -1

def main(argc:int,argv:[str]) -> None:
    if(argc != 2):
        raise UsageError(f'correct usage : {argv[0]} dir name')

    try :
        for(dir_name,subdir_list,nondir_list) in os.walk(argv[1]):
            print(f'Directory : {dir_name}')
            if(len(subdir_list) >0):
                print(f'\t SUB DIRECTORIES ')
                for subdir_name in subdir_list:
                    print('\t\t{subdir_name}')
            if(len(nondir_list)>0):
                print(f'\t NON directories :')
                for non_dir in nondir_list:
                    print(f'\t\t{non_dir}')
    except :
        exc_name,exc_data,exc_tb = sys.exec_info()
        print('could not walk through given directory becasue ')
        print(exc_name.__name__,exc_data,sep=':',flush=True)
    sys.exit(EXIT_SUCCESS)

main(len(sys.argv),sys.argv)

    