from functools import cmp_to_key

def largestNumber(nums):
    words = []
    #converting list of int into string
    for indx,elt in enumerate(nums):
        nums[indx]=str(elt)
       
    def compare(n1,n2):
        if n1+n2>n2+n1:
            return -1
        else:
            return 1
    res = sorted(nums, key = cmp_to_key(compare))
  
    return ''.join(res)
if __name__ == "__main__":
    # n=int(input("Enter the number of elements: "))
    print("Enter the elements: ")
    nums=list(map(int,input().split()))
    print("Largest number formed is: ",largestNumber(nums))
