#include <bits/stdc++.h>
using namespace std;

#define ll long long


int main(){
	ll N; cin >> N;
	ll a[N];
	ll ans =0;
	for(int i=0;i<N;i++){
		cin >> a[i];
		ans ++;
	}

	for(int i=0;i<N;i++){
		ll p = a[i];
    ll seqcount = 0;
		for(int j=i+1;j<N;j++){
			if(p<a[j]){
        seqcount++;
				// cout << "(" << i << j << ")" << endl;
				ans+=seqcount;
				p = a[j];
			}
			else break;
		}
    i += seqcount;
	}
	cout << ans << endl;
	return 0;
}
// 6
// 1 2 3 2 1 2
// 5
// 1 2 3 1 2
