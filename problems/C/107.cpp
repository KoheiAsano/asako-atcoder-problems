#include <bits/stdc++.h>
using namespace std;


int N,K;

int dx[2] = {1,-1};

const int INF = 2000000000;
int main(){
	cin >> N >> K;
	int x[N];
	int d[N];
	for(int i=0;i<N;i++){
		cin >> x[i];
		d[i] = abs(x[i]);
	}
	int ans=INF;
		for(int i=0;i<N-K+1;i++){
			int mid = abs(x[i] - x[i+K-1]);
			ans = min(min(d[i],d[i+K-1]) + mid, ans);
		}
	cout << ans << endl;
	return 0;
}
