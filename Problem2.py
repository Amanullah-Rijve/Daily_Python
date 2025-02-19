
 x = 2
 y = 3
 z = x ** y + y ** x
 print(z)


 def string_mainpulation(s):
     s = s.replace('a' , 'b')
     s = s.replace('b' , 'c')
     s = s.replace('c' , 'a')
     return s

 s ="abcabc"
 print(string_mainpulation(s))
    


 def myFun(num):
   return num*2

 result = myFun(2)
result = myFun(result)
 result = myFun(result)
 result = myFun(result)
 print(result)
