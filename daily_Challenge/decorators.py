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

def palindrome(func):
    def wrapper(func):
        left=0
        right=len(func)-1
        while left<=right:
            if func[left]==func[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    return wrapper
def revers(func):
    def wrapper(txt):
        txt = list(txt)  # Convert txt to a list of characters
        left = 0
        right = len(txt) - 1
        while left <= right:
            txt[left], txt[right] = txt[right], txt[left]
            left += 1
            right -= 1
        txt = ''.join(txt)  # Convert the list of characters back to a string
        return txt
    return wrapper



        
def makePretty(func):
    def Inner():
        print("I got decorated")
        func()
    return Inner
@makePretty
def test():
    print("I am an ordinary")
test()

def splitter(func):
    def wrapper():
        return list(func())
    return wrapper
def reverse(func):
    "reverse function reverses the array using built in method"
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


# Python Function Arguments
def defaultVal(a=8,b=9):
    "Function Argument with Default Values In computer programming, an argument is a value that is accepted by a function."
    res=a+b
    return print('Sum :',res)

defaultVal()
defaultVal(b=5)
defaultVal(5,23)

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum = ", result)
def find_mul(a,b,*numbers,**args):
    result = a*b
    for i in numbers:
        result = i*result
    for k,v in args.items():
        result=v*result
    print("mul = ", result)

find_sum(1,3,4,5,6,90)
find_sum(1,3,4,5)
find_mul(4,5,g=6,k=2,l=5)
