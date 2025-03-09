def total_even(a, b):
    Sum = 0  
    for even in range(a, b):
        if even % 2 == 0:
            Sum += even 
    print("The Total Sum of Even Numbers is:", Sum)

total_even(1, 20)
total_even(10, 50)
total_even(35, 90)
