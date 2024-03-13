#include iostream

void solve(){
    int n; std::cin >> n;
    for(int i = 1 ,nouse ; i <= n ; ++i){
        std::cin >> nouse;
    }
    std::cout << "1 " << n << std::endl;
}

int main(){
    int t; std::cin >> t;
    while(t--) solve();
    return 0;
}