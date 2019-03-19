#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll N;

ll memo[100];
ll luka(ll n) {
	if(n == 0) return 2;
	else if (n == 1) return 1;
	else if (memo[n]!=0) return memo[n];
	else return memo[n] = luka(n-1) + luka(n-2);
}


int main(){
	cin >> N;
	ll ans = luka(N);
	cout << ans << endl;
	return 0;
}
