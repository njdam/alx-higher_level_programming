#!/usr/bin/python3
# A script to print all names in hidden_4.pyc file except name start with "__"

if __name__ == "__main__":
    import hidden_4
    argv = dir(hidden_4)
    argc = len(argv)

    for i in range(argc):
        if argv[i][:2] != "__":
            print("{}".format(argv[i]))
