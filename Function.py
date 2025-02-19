 def simple(a):
    for i in a:
         print(i)
         if(i==10):
             print("Loop ended")
             break
            
 print(simple(range(1,11)))


 def calculate (a,b):
     sum= a+b
     return sum   

 print("The sum is: ", calculate(5,5))
