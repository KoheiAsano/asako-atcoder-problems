#include <bits/stdc++.h>
using namespace std;

int N, D, X;


int main(){

	cin >> N;
	cin >> D >> X;
	int A[N];
	int ans=X;
	for(int i=0; i<N;i++) {
		cin >> A[i];
		int tmp = A[i];
		A[i]++;
		ans++;
		while(A[i]<=D){
			// cout << A[i] << endl;
			ans++;
			A[i]+=tmp;
		}
	}
	cout << ans << endl;

	return 0;
}
