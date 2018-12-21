#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll N,x;
int main(){
	cin >> N >> x;
	ll a[N];
  ll ans=0;
	for(int i=0;i<N;i++){
		cin >> a[i];
    if(a[i]>x){
			int difff = a[i] - x;
      a[i]-= difff;ans+=difff;
    }
	}
  for(int i=0;i<N-1;i++){
		if(a[i]+a[i+1]>x){
			int diff = a[i]+a[i+1] - x;
			a[i+1]-= diff;ans+=diff;
		}
  }
	cout << ans << endl;
	return 0;
}
