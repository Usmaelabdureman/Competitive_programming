import math
lst=[[1,3],[-2,2]]
# out=[[]]
def test(lst):
    for i in lst[0:len(lst)-1]:
        for j in lst[1:len(lst)]:
            if i[0]**2+i[1]**2 < j[0]**2+j[1]**2:
                temp=i
                i=j
                j=temp
    # return 
for i in lst:
    for j in lst:
        # if i[0]**2+i[1]**2 < j[0]**2+j[1]**2:
            temp=i
            i=j
            j=temp
    print(temp)
    print(lst)


