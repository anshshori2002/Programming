# This is the type of Calculator in Which we can reuse the previous calulated answer for solving. 
# --------------------------------------------------------Code Starts-----------------------------------------------------------------------------

#Functions to Store Answer
def answer (ans):
    print("1.   Add")
    print("2.   Subtract")
    print("3.   Product")
    print("4.   Division")
    print("5.   Exponent")
    n = int(input("Enter choice you want to do with previous answer: "))
    q=int(input("Enter Another no.:"))
    if(n==1): addition(ans,q)
    elif(n==2): subtract(ans,q)
    elif(n==3): multiply(ans,q)
    elif(n==4): division(ans,q)
    elif(n==5): expo(ans,q)
    else: print("Please Enter correct option. ")


#Function for Addition
def addition(x,y):
    sum = x + y
    print("Addition:",sum)
    a=input("Continue with Answer(Y/N)?")
    if a=='Y'or a=='y' :
        answer(sum)


#Function for Subtraction 
def subtract(x,y):
    sub = x - y
    print("Subtraction: ",sub)
    a=input("Continue with Answer(Y/N)?")
    if a=='Y'or a=='y' :
        answer(sub)


#Function for Multiplication
def multiply(x,y):
    product = x * y
    print("Product:",product)
    a=input("Continue with Answer(Y/N)?")
    if a=='Y'or a=='y' :
        answer(product)


#Function for Division
def division(x,y):
    if(y > x):
        division = x / y
        print("Division:",division)
        a=input("Continue with Answer(Y/N)?")
        if a=='Y'or a=='y':
            answer(division)
    else:
        division = x // y
        print("Division:",division)
        a=input("Continue with Answer(Y/N)?")
        if a=='Y'or a=='y':
            answer(division)


#Function for Exponential    
def expo(x,y):
    exponent = x ** y
    print("Exponent:",exponent)
    a=input("Continue with Answer(Y/N)?")
    if a=='Y'or a=='y':
        answer(exponent)


def end():
    quit()


""" Calculator """
while(1):
    print("____Calculator____")
    print(" ")
    print("1.   Add")
    print("2.   Subtract")
    print("3.   Product")
    print("4.   Division")
    print("5.   Exponent")
    print("6.   EXIT")
    
    choice = int(input("Enter your choice: "))
    if(choice == 6):
        print("!!Thanks for Using!!\n");end()
    a = int(input("Enter the First no.: "))
    b  = int(input("Enter the Second no.: "))
    if (choice == 1):
        addition(a,b)
    elif (choice == 2):
        subtract(a,b)
    elif (choice == 3):
        multiply(a,b)
    elif (choice == 4):
        division(a,b)
    elif (choice == 5):
        expo(a,b)
    else:
        print("Please Enter Correct option ")
        
        
#    -----------------------------------------------------------Code Ends----------------------------------------------------------------------------

# OUTPUT:

# ____Calculator____
 
# 1.   Add
# 2.   Subtract
# 3.   Product
# 4.   Division
# 5.   Exponent
# 6.   EXIT
# Enter your choice: 1
# Enter the First no.: 23 
# Enter the Second no.: 44
# Addition: 67
# Continue with Answer(Y/N)?y
# 1.   Add
# 2.   Subtract
# 3.   Product
# 4.   Division
# 5.   Exponent
# Enter choice you want to do with previous answer: 2
# Enter Another no.:34
# Subtraction:  33
# Continue with Answer(Y/N)?y
# 1.   Add
# 2.   Subtract
# 3.   Product
# 4.   Division
# 5.   Exponent
# Enter choice you want to do with previous answer: 4
# Enter Another no.:3
# Division: 11
# Continue with Answer(Y/N)?n
# ____Calculator____

# 1.   Add
# 2.   Subtract
# 3.   Product
# 4.   Division
# 5.   Exponent
# 6.   EXIT
# Enter your choice: 6
# !!Thanks for Using!!
        
