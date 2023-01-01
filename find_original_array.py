
def findOriginalArray(changed):
    arr_len=len(changed)
    mydict={}
    for i in changed:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    changed.sort()
    result=[]
    for i in range(arr_len):
        freq=mydict[changed[i]]
        if freq>0:
            result.append(changed[i])
            doubled=2*changed[i]
            mydict[changed[i]]-=1
            mydict[doubled]-=1
    return result
        

ts=[1,3,4,2,6,8]
tj=[2,1]
ts4=[0,3,2,4,6,0]
l=len(ts4)
print(findOriginalArray(ts))
print(findOriginalArray(tj))
print(findOriginalArray(ts4))

        
