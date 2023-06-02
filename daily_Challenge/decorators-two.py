from decorators import *

@revers
def test(wd):
    pass
@palindrome
def Check(func):
    pass
print(Check("racecar"))
print(Check("raceca"))
print(test("test"))
print(test("123456"))
