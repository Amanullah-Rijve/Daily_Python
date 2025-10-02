# # control Flow

'''
1.Write a program that asks the user to input
a number and prints whether the number is positive.
2.Write a program that asks the user to input a number and prints whether
the number is positive or negative.
3. Write a program that asks the user to input a number and prints whether the number 
is positive, negative, or zero.
'''

#  n = int(input("Enter a integer number: "))

# if(n<0):
#     print(f"{n} is negetive")
# elif(n==0):
#     print(f"{n} is 0")
# else:
#     print(f"{n} is possitive")   

'''
4.Write a program that asks the user to input a number and prints 
whether the number is positive and even, positive and odd, or negative.
'''    

# n = int(input("Enter a integer: "))

# if n > 0:
#     if n % 2 == 0:
#         print(f"{n} is positive and even")
#     else:
#         print(f"{n} is positive and odd")
# elif n < 0:
#     print(f"{n} is negative")
# else:
#     print("The number is zero")

'''
5. Write a program that prints all the numbers 
from 1 to 10 using a for loop.
'''
# for i in range(1,11):
#     print(i)

'''
6.Write a program that prints all the numbers
from 1 to 10 using a while loop.
'''

# i =  1
# while(i<=10):
#     print(i)

'''
7.Write a program that prints a 5x5 grid 
of asterisks (*) using nested loops.
'''

for i in range(5):
    for j in range(5):
        print("*",end="")
    print()    