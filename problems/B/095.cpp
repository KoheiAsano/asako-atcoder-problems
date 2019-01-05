#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000

int N,  X;

int main(){
	cin >> N >> X;
	int m[N];
	int mass = INF;
	int ans =0;
	for(int i=0;i < N;i++){
		cin >> m[i];
		mass = min(mass,m[i]);
		X-=m[i];ans++;
	}
	while(X>=mass){
		X-=mass;ans++;
	}
	cout << ans << endl;
	return 0;
}
