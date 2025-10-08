def even(x):
    return x%2==0

numbers = [1,2,3,4,5,6,7,8,9,10]
evebs = list((filter(even,numbers)))

print(evebs)

#  using lambda with filter

number = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda x: x%2==0,number))

print(evens)