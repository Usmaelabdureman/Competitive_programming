t=int(input())
s=list(map(int,input().split()))

odd =[x for x in s if x%2==1]

max_even=sum(s)
min_num=0
if len(odd)%2==1:
    min_num=min(odd)
if max_even%2!=0:
    max_even=max_even-min_num
print(max_even)
    
        