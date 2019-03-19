#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;
typedef long long ll;
ll W,H;

ll mod_pow(ll x, ll n, ll mod){
	ll res=1;
	while(n>0) {
		if(n&1){res=res*x%mod;}
		x=x*x%mod;
		n>>=1;
	}
	return res;
}


int main(){
	cin >> W >> H;
	ll ans=1;
	ll a=1, b = 1;
	for(int i=1;i<=W+H-2;i++){ans=ans*i%MOD;}
	for(int i=1;i<=W-1;i++){a=a*i%MOD;}
	for(int i=1;i<=H-1;i++){b=b*i%MOD;}
	a=mod_pow(a,MOD-2,MOD);
	b=mod_pow(b,MOD-2,MOD);
	cout << ans*a%MOD*b%MOD << endl;
	return 0;
}
