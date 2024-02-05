"""
outputstandard output
A2SV's opening and closing ceremonies are renowned for their enjoyment and memorability. Often, these events feature snacks, beverages, and games. However, once the ceremonies conclude, there is generally no one available to handle the clean-up. One A2SVian consistently steps up to this task: Beza.

In the most recent ceremony, the clean-up involved numerous items, which consumed a considerable amount of her time. Beza employed a trash bag to gather all the discarded items. During the process, she observed that each item she picked up had a weight of either A
 or B
. Her trash bag could accommodate items up to a maximum weight of S
. Additionally, Beza was aware of the value associated with each item.

In order to infuse some interest into the clean-up, she set herself a challenge: What is the maximum total value of the items the trash bag can hold? By the conclusion of the clean-up, she had successfully arrived at the answer and felt a sense of accomplishment.

Could you have successfully tackled this problem as well?

Input
The first line contains integers n,m,s,A,
 and B
 (1≤n,m≤105
, 1≤s,A,B≤109
).

The second line contains n
 integers, ai
(1≤ai≤109
) where ai
 is the value of the ith
 item. Each of them weigh A
.

The third line contains m integers bi
(1≤bi≤109
) where bi
 is the value of the ith
 item. Each of them weigh B
.

Output
Print one number: the maximum total cost of items that can be put in a trash bag.

Example
inputCopy
6 7 23 3 5
7 4 3 1 5 8
10 12 7 3 8 9 7
outputCopy
47
Note
In the first example, from the items that weigh A
, we can pick items with cost 8
 and from items that weigh B
, we can pick items with costs 9,10,12,8
.

— a problem by, Biruk Zewdu

    """
    
##Solution

n,m,s,A,B=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
a.reverse()

b.reverse()
sum=0
i=0
j=0
while(i<n and s>=A):
    s-=A
    sum+=a[i]
    i+=1
while(j<m and s>=B):
    s-=B
    sum+=b[j]
    j+=1
print(sum)
