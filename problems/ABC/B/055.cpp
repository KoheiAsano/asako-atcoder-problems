
#include <bits/stdc++.h>
#define MOD 1000000007
using namespace std;
typedef long long ll;


ll fact(ll n){
	if(n==1) return 1;
	else return (n * fact(n-1))%MOD;
}
int n;
int main(){
	cin >> n;
	cout << fact(n)  << endl;
	return 0;
}
