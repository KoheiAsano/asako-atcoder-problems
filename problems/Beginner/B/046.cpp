#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll N,K;

int main(){
	cin >> N >> K;
	ll ans = K;
	for (int i = 0;i<N-1;i++){
		ans*=K-1;
	}
	cout << ans << endl;
}
