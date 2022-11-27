def largestNumber(nums):
    nums=(str(i) for i in nums)
    pass

st=[1,20,4,5]
ls=[]
for i in range(len(st)):
    ls.append(str(st[i]))

res=''.join(ls)
output=[]
for j in res:
    output.append(int(j))

output.sort(reverse=True)

print(output)