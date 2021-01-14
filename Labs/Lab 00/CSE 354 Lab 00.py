#############################################################################
# Program:
#    Lab 0, Practice Lab Submission
#    Brother Jones, CSE 354
# Author:
#    Whitney LeSueur
# Summary:
#    This program will accept user input and, depending on input, will
#    either return a message and ask for user input again or return a 
#    message and terminate the program.
#############################################################################
#############################################################################
#
# Changes made to my code for the Lab 0 Take-2:
#   (examples:)
#   - Filled out main comment block below.
#
#############################################################################
import sys

#############################################################################
# Return a statement, close program, or both, depending on user input. 
#############################################################################
DEFAULT_VALUE = 'n'
arg1 = sys.argv[1] if len(sys.argv) == 2 else DEFAULT_VALUE


try:
    #Your code starts here
    print('Hello World!')
    arg1 == "n"
    while arg1 == "n" or "r":
        arg1 = input('Input n, r, or q: ')

        if arg1 == "n":
            print('Hello World!')
        elif arg1 == "r":
            print("World Hello!")
        else:
            print('All done!')
            quit()

except KeyboardInterrupt:
    print('\nShutting down ...')