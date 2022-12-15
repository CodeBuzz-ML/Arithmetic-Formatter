"""
Author: CodeBuzz
Language: Python 3.11.0 64-bit
Project Name: Arithmetic Formatter

Main Function: format(num1,num2,operation,ansOrNot)
"""
def format(num1,num2,operation,ansOrNot):
    
    #inputing the vals
    if operation == "+":
        sum = num1+num2
        if ansOrNot == True:
            print(" ",end="  ")
            print(num1)
            print("+",end="  ")
            print(num2)
            print("----------")
            print("  ",sum)
            print("----------")
        
        elif ansOrNot == False:
            print(" ",end="  ")
            print(num1)
            print("+",end="  ")
            print(num2)
            print("----------")
            print(" ")
            print("----------")
    if operation == "-":
        diff = num1-num2
        if ansOrNot == True:
            print(" ",end="  ")
            print(num1)
            print("-",end="  ")
            print(num2)
            print("----------")
            print("  ",diff)
            print("----------")
        
        elif ansOrNot == False:
            print(" ",end="  ")
            print(num1)
            print("-",end="  ")
            print(num2)
            print("----------")
            print(" ")
            print("----------")
    if operation == "*":
        prod = num1*num2
        if ansOrNot == True:
            print(" ",end="  ")
            print(num1)
            print("*",end="  ")
            print(num2)
            print("----------")
            print("  ",prod)
            print("----------")
        
        elif ansOrNot == False:
            print(" ",end="  ")
            print(num1)
            print("*",end="  ")
            print(num2)
            print("----------")
            print(" ")
            print("----------")
        
    if operation == "/":
        quot = num1/num2
        if ansOrNot == True:
            print(" ",end="  ")
            print(num1)
            print("/",end="  ")
            print(num2)
            print("----------")
            print("  ",quot)
            print("----------")
        
        elif ansOrNot == False:
            print(" ",end="  ")
            print(num1)
            print("/",end="  ")
            print(num2)
            print("----------")
            print(" ")
            print("----------")
    if operation == "^":
        exp = num1 ** num2
        if ansOrNot == True:
            print(" ",end="  ")
            print(num1)
            print("^",end="  ")
            print(num2)
            print("----------")
            print("  ",exp)
            print("----------")
        
        elif ansOrNot == False:
            print(" ",end="  ")
            print(num1)
            print("^",end="  ")
            print(num2)
            print("----------")
            print(" ")
            print("----------")
