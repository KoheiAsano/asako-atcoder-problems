#include <bits/stdc++.h>
using namespace std;
#define ll long long

#define MOD 1000000007
int fact(int n){
	if(n == 1) return 1;
	else return n*fact(n-1);
}

int N;
ll bucket[1001] = {0};
int main(){
	cin >> N;

	for (int i=2;i<N+1;i++){
		int n = i;
		for(int j=2;j<=i;j++){
			while(n % j == 0){
				n /= j;
				bucket[j]++;
			}
		}
	}
	ll ans = 1;
	for(int i=2;i<N+1;i++){
		// cout << bucket[i] << endl;
		if(bucket[i] != 0)ans = ans *(bucket[i] + 1) % MOD;
	}
	cout << ans % MOD << endl;
	return 0;
}
