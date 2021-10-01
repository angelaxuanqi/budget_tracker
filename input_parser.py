#!/usr/bin/python

import sys

def parse_user_input(num_args, argv):
    if num_args != 0:
        if argv[1] == "spent":
            print("-----> User types spent")
        else:
            print("Please type spent or deposit, thanks!")
            sys.exit()
    else:
        print("!!!! No inputs!!!!")
        sys.exit()
    

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
parse_user_input(len(sys.argv), sys.argv)
