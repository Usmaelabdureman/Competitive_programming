"""
     Flower City Fence
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Anya lives in the Flower City. By order of the city mayor, she has to build a fence for herself.

The fence consists of n
 planks, each with a height of ai
 meters. According to the order, the heights of the planks must not increase. In other words, it is true that ai≥aj
 for all i<j
.

Anya became curious whether her fence is symmetrical with respect to the diagonal. In other words, will she get the same fence if she lays all the planks horizontally in the same order.

For example, for n=5
, a=[5,4,3,2,1]
, the fence is symmetrical. Because if all the planks are laid horizontally, the fence will be [5,4,3,2,1]
, as shown in the diagram.


On the left is the fence [5,4,3,2,1]
, on the right is the same fence laid horizontally

But for n=3
, a=[4,2,1]
, the fence is not symmetrical. Because if all the planks are laid horizontally, the fence will be [3,2,1,1]
, as shown in the diagram.


On the left is the fence [4,2,1]
, on the right is the same fence laid horizontally

Help Anya and determine whether her fence is symmetrical.

Input
The first line of the input contains an integer t
 (1≤t≤104
) — the number of test cases.

The description of the test cases follows.

The first line of a test case contains a single integer n
 (1≤n≤2⋅105
) — the length of the fence.

The second line of a test case contains n
 integers a1≥a2≥a3≥⋯≥an
 (1≤ai≤109
) — the heights of the planks.

The sum of the values of n
 for all test cases does not exceed 2⋅105
.

Output
For each test case, output "YES" if the fence is symmetrical, otherwise output "NO".

You can output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes" and "YES" will be accepted as a positive answer.

Example
inputCopy
7
5
5 4 3 2 1
3
3 1 1
3
4 2 1
1
2
5
5 3 3 1 1
5
5 5 5 3 3
2
6 1
outputCopy
YES
YES
NO
NO
YES
YES
NO
Note
In the first and second test cases of the example, the fence is symmetrical.

In the third test case of the example, the fence is not symmetrical. If the planks are laid horizontally, the fence will be [3,2,1,1]
.

In the fourth test case of the example, the fence is not symmetrical. If the planks are laid horizontally, the fence will be [1,1]
.

In the fifth and sixth test cases of the example, the fence is symmetrical.

In the seventh test case of the example, the fence is not symmetrical. If the planks are laid horizontally, the fence will be [2,1,1,1,1,1]
. 

"""

# SOLUTION


# Accepted solution which touches all edge cases
# code is self explanatory

# time complexity is O(n)

# space complexity is O(1)


"""
    

#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    
    #ifndef ONLINE_JUDGE
    freopen("input1.txt", "r", stdin);
    freopen("/Users/sreejith/Desktop/output.txt", "w", stdout);
    #endif
    int t;
    cin>>t;
    while(t--){
         ll n;
         cin>>n;
         vector < ll > v(n+1), rotated(n+1);
         for(ll i = 1 ; i <= n ; i++) { 
            cin>>v[i];
         }
         if(v[1] != n) {
            cout<<"NO\n";
            continue;
         }
         for(ll i = 1 ; i <= n ; i++) {
            rotated[v[i]]++;
         }
         for(ll i = n-1 ; i >= 1 ; i--) {
            rotated[i]+=rotated[i+1];
         }
         if(rotated == v)
            cout<<"YES";
         else
            cout<<"NO";
         cout<<endl;
    }       
    return 0;
}


    """



t = int(input())
for _ in range(t):
    n = int(input())
    v = [0] * (n+1)
    rotated = [0] * (n+1)
    for i in range(1, n+1):
        v[i] = int(input())
    if v[1] != n:
        print("NO")
        continue
    for i in range(1, n+1):
        rotated[v[i]] += 1
    for i in range(n-1, 0, -1):
        rotated[i] += rotated[i+1]
    if rotated == v:
        print("YES")
    else:
        print("NO")
