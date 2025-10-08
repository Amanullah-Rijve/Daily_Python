def sqr(x):
    return x*x

number = [1,2,3,4,5,6,7,8,9,10]
square = list(map(sqr,number))

print(square)

# map with lambda function 

numbers = [1,2,3,4,5,6,7,8,9,10]
list(map(lambda x:x*x,numbers))

print(numbers)

#  multiple iteration using map

number1 = [1,2,3,4]
number2 = [5,6,7,8]

added_num = list(map(lambda x,y: x+y,number1,number2))

print(added_num)

# type casting with map

my_list = ['1','2','3','4','5']
convert_int = list(map(int,my_list))

print(convert_int)