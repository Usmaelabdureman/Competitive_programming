"""
#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

void testcase(){
    ll n,m;
    cin>>n>>m;

    for(ll i=1;i<=n;i++){
        for(ll j=1;j<=m;j++){
            cout<<((i%4<=1)!=(j%4<=1))<<" \n"[j==m];
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t;
    cin>>t;
    while(t--)
        testcase();
    return 0;
}
"""