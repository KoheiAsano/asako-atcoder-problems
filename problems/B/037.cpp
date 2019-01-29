#include <bits/stdc++.h>
using namespace std;


int N,Q;


int main(){
	cin >> N >> Q;
	int A[101] = {0};
	int L[Q], R[Q], T[Q];
	for (int i = 0;i<Q;i++){
		cin >> L[i] >> R[i] >> T[i];
		for (int j = L[i]-1;j<R[i];j++)A[j] = T[i];
	}
	for (int i=0;i<N;i++){
		cout << A[i] << endl;
	}
}
