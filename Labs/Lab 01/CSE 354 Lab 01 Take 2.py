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
#############################################################################
#
# Changes made to my code for the Lab 1 Take-2:
#   - Spent time learning more about Python file reading capabilities
#   - Implemented code to translate the file by reading as opposed to 
#     returning pre-translated text.
#
#############################################################################

import sys

#############################################################################
# Return Hexadecmial code for a given file containing Machine Language.
#############################################################################

def fileSelect():
    filename = ''
    while filename == '':
        fileRequest = input("Please select which file you wish to translate: \n1] ECEN160_test1.txt \n2] ECEN160_test1.txt\n> ")
        if fileRequest == '1':
            filename = 'ECEN160_test1.txt'
        elif fileRequest == '2':
            filename = 'ECEN160_test2.txt'
        else:
            print("Please enter a valid file selection number!")
    try:
        f = open(filename, 'r')
        fileContent = f.read()
        return fileContent
    except KeyboardInterrupt:
        print('\nInvalid filename!')

def convertMachineLang(fileContent):
    count = 0
    x = []
    for n in fileContent:
        if n == 'L':
            x.append('1')
        elif n == 'A':
            nextChar = fileContent[count+1]
            if nextChar == 'D':
                x.append('7')
        elif n == 'S':
            x.append('30')
        elif n == ',':
            nextChar = fileContent[count+2]
            if nextChar != 'r':
                x.append('0')
                x.append(nextChar)
        elif n == 'r':
            nextChar = fileContent[count+1]
            x.append(nextChar)
        elif n == '\n':
            prevChar = fileContent[count-10]
            if prevChar == 'M':
                x.append('0')
            x.append('\n')
        elif n == 'N':
            x.append('0000')
        elif n == 'M':
            x.append('2')
        count += 1
    return x

def printHexadecimal(machineLang):
    for n in machineLang:
        print(n, end='')
    print()
    
def main():
    fileContent = fileSelect()
    machineLang = convertMachineLang(fileContent)
    printHexadecimal(machineLang)

if __name__ == "__main__":
    main()