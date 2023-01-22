#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argv = len(argv)

    if argv == 1:
        print("0 arguments.", end="")

    elif argv == 2:
        print("{} argument:".format(argv[i]))
    
    else:
        print("{} arguments:".format(argv[i]))


    for i in range(1, argv):
        print("{}: {}".format(i, argv[i]))
