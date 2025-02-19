

#!find its and alphabet or not

 a = str(input("Enter An Alphabet:"))
 print("You have Enterd:",a)

 if(a>='a' and a<='z'):
     print("This is a lowercase alphabet")
 elif(a>='A'and a<='Z'):
     print("This a uppercase alphabet")
 else:
     print("THis is  not an alphabet")


#! find even or odd

 a = int(input("Enter a number:"))
 print("The Number You Enterd is:",a)

 if(a % 2 == 0):
     print("The Number is Even")
 else:
     print("The Number is odd")


# !find the largest number

 a = int(input("Enter First Number: "))
 b = int(input("Enter second Number: "))
 c = int(input("Enter third Number: "))

 print("The Numbers Are: ",a,b,c)

if(a>b and a>c):
  print("first Number is Largest")
 elif(b>a and b>c):
    print("second Number Is largest")
 elif(a==b  or b==c or c==b):
     print("All Numbers Are Equal")
 else:
     print("Third Number is largest")

