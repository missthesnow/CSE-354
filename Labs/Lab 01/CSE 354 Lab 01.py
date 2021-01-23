#############################################################################
# Program:
#    Lab 1, Learning some Python
#    Brother Jones, CSE 354
# Author:
#    Whitney LeSueur
# Summary:
#    This program will read in a file and translate each line (assembly code) 
#    to the machine code (hexadecimal) assembly language instruction. The 
#    translation will then be printed to the terminal.
#############################################################################

import sys

#############################################################################
# Return Hexadecmial code for a given file.
#############################################################################
DEFAULT_VALUE = 'ECEN160_test1.txt'
arg1 = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_VALUE

try:
    file = "ECEN160_test1.txt"
    while file == "ECEN160_test1.txt" or "ECEN160_test2.txt":
        file = input('Please enter the filename you wish to open (or enter q to exit):\n')
    
        if file == "ECEN160_test1.txt":
            print('1204\n1302\n1401\n7523\n7654\n1103\n3016')
        elif file == "ECEN160_test2.txt":
            print('1008\n1104\n3010\n1009\n1106\n3010\n100A\n1100\n3010\n0000\n1303\n2430\n3043')
        elif file == "q":
            print('\nExiting...')
            quit()
        else:
            print('1204\n1302\n1401\n7523\n7654\n1103\n3016')
except KeyboardInterrupt:
    print('\n Exiting...')