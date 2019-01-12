#include <bits/stdc++.h>
#define ll long long
using namespace std;


int N;
int F[101][15];
int P[101][14];
ll one( ll b){
	ll sum=0;
	for (int i=0;i<N;i++){
		ll c = 0;
		for(int j=0;j<10;j++)if((b>>j&1)&&F[i][j])c++;
		sum+=P[i][c];
	}
	return sum;
}

int main(){
	cin >> N;

	for(int i=0;i<N;i++){
		for(int j=0;j<10;j++){
			cin >> F[i][j];
		}
	}

	for(int i=0;i<N;i++){
		for(int j=0;j<11;j++){
			cin >> P[i][j];
		}
	}
	ll ans=-2000000000;
	for(int b=1;b<(1 << 10);b++){
		ans = max(ans,one(b));
	}
	cout << ans << endl;
}
