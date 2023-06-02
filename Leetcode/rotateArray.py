
def rotate(arr,shiftby):
    ans=[0]*len(arr)
    
    for i in range(len(arr)):
        ans[(i+shiftby)%len(arr)]=arr[i]
    return ans

if __name__ == "__main__":
    ar=[1,2,3,4,5,6]
    k=2
    print(rotate(ar,k))
    print(1%6)