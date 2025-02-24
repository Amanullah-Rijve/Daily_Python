nestefd funcction

def outer(x):
    def inner(y):
        return x + y
    return inner

add_num1 = outer(10)
sum = add_num1(7)
print(sum)

!Pass Function as Argument

def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result) 


Return a Function as a Value

def get_name(name,occ,age):
    def hello():
        return "Hi I am " + name + " and I am a " + occ + "i am " + str(age) + " years old"
    return hello

get1 = get_name("Amanullah","Developer",23)
get2 = get_name("Rijve","Gammer",17)
get3 = get_name("Topon","Accounter",25)

print(get1())
print(get2())
print(get3())

! Python Decorators

def make_new(func):
    def inner():
        print("I got new bike")
        func()
    return inner


def ordinary():
    print("I am rijve")

! @ Symbol With Decorator

def make_new(call):
    def inner():
        print("Hello there")
        call()
    return inner

@make_new
def hi_there():
        print("Hi There")

def welcome():
     print("Welconme To Bangladesh")

hi_there()
welcome()  

def smart_div(div):
    def inner(x,y):
        print("I am going to devide", x, "and", y )
        if y ==0:
            print("Can not devide")
            return
        return div(x,y)
    return inner

@smart_div
def devide(x,y):
    print(x/y)

devide(5,10)
devide(45,19)
devide(523,46)
devide(5,6)
devide(2,14)
devide(2,0)

! Chaining Decorators in Python

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
