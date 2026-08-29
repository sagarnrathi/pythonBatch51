import sys

EXIT_SUCCESS = 0
EXIT_FAILURE = -1

def main(argc:int,argv:[str])->None:
    print('argc : ',argc)
    print('argv : ',argv)

    sys.exit(EXIT_SUCCESS)

main(len(sys.argv),sys.argv)
