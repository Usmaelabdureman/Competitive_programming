#  Assigning functions to variables
def plus_ten(number):
    return number+10
vars =plus_ten

print(vars(10))
# Defining function inside other functions

def Add_one(number):
    def plus_one(number):
        return number+1
    result = plus_one(number)
    return result
print(Add_one(4))

# Passing functions as arguments to other functions
def mul_by_five(num):
    return num * 5
def add_five(num):
    return num + 5

def fnCall(func,func2):
    numtoAdd = 30
    
    return func(numtoAdd)+func2(numtoAdd)

print(fnCall(mul_by_five,add_five))

def Add(a,b):return a+b
def Mul(a,b):return a*b
def Sub(a,b):return a-b
def Div(a,b):return a/b

def calculate(func,a,b):return func(a,b)

result1=calculate(Add,4,6)
result2=calculate(Mul,4,6)

print(result1)
print(result2)

# functions returning other functions

def hello_func():
    "this is hello function"
    # another comment here
    def say_Hi():
        return "Hi"
    return say_Hi
dc=hello_func.__doc__
print(dc)
hello = hello_func()
t=hello()
print(t)

# Nested Functions have acces to the enclosing function's variable Scope
def greeting(name):
    "enclosing function"
    def message_sender():
        "nested function"
        print("Hello,"+name+"!")
    return message_sender()

greeting("Usmael")

# decorator example
def makePretty(func):
    def Inner():
        print("I got decorated")
        func()
    return Inner
@makePretty
def test():
    print("I am an ordinary")
test()

def splitter(word):
    def wrapper():
        return list(word())
    return wrapper
def reverse(func):
    def wrapper():
        return func()[::-1]
    return wrapper
def join(lst):
    def wrapper():
        return "".join(lst())
    return wrapper
def upper_case(func):
    def wrapper():
        return func().upper()
    return wrapper

@upper_case 
@join
@reverse
@splitter
def test():
    return "Hello"
print(test())