

def reverse_list_decorator(func):
    def wrapper(txt):
        left,right = 0,len(txt)-1
        while left < right:
            txt[left],txt[right] = txt[right],txt[left]
            left += 1
            right -= 1
        return func(txt)  # Added return statement to call the original function
    return wrapper

@reverse_list_decorator
def main(txt):  # Added parameter to the main function
    print(txt)