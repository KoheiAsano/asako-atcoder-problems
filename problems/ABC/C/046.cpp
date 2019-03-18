#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll N;
ll T[1001],A[1001];
int main(){
	cin >> N;
	for(int i=0;i<N;i++){
		cin >> T[i] >> A[i];
	}

	ll Tp=1, Ap=1;
	ll n = 1;//比と最小値の倍率
	for(int i=0;i<N;i++){
		ll tmpT = Tp/T[i];ll tmpA = Ap/A[i];
		if(Tp%T[i] != 0){
			tmpT ++;
		}
		if(Ap%A[i] != 0){
			tmpA ++;
		}
		n = max(tmpT,tmpA);
		Tp = T[i]*n;Ap = A[i]*n;
	}
	cout << Tp + Ap << endl;
}
