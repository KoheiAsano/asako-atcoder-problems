#include <bits/stdc++.h>
using namespace std;



int N, M, X;

int main(){
	cin >> N >> M >> X;
	int A[M];
	int l=0, r=0;
	for(int i=0;i < M;i++){
		cin >> A[i];
		if(A[i] < X)l++;
		else if(A[i] > X)r++;
	}
	cout << min(l,r) << endl;
	return 0;
}
