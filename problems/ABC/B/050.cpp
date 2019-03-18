#include <bits/stdc++.h>
using namespace std;


int N,M;

int main(){
	cin >> N;
	int T[N+1];
	for(int i=0;i<N;i++){
		cin >> T[i];
	}
	cin >> M;
	int P[M+1],X[M+1];
	for(int i=0;i<M;i++){
		cin >> P[i] >> X[i];
	}
	for(int i=0;i<M;i++){
		int ans=0;
		for(int j=0;j<N;j++){
			if(j == P[i]-1)ans+=X[i];
			else ans+=T[j];
		}
		cout << ans << endl;
	}
	return 0;
}
