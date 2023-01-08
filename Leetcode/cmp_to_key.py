from functools import cmp_to_key

def largestNumber(nums):
    #converting list of int into string
    for i,j in enumerate(nums):
        nums[i]=str(j)
    def compare(n1,n2):
        if n1+n2 > n2+n1:
            return -1
        else:
            return 1
    res=sorted(nums,key=cmp_to_key(compare))
    return res

if __name__ == "__main__":
    n=int(input("Enter the number of elements: "))
    print("Enter the elements: ")
    nums=list(map(int,input().split()))
    print("Largest number is: ",largestNumber(nums))