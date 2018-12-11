#include <bits/stdc++.h>
using namespace std;


int N,M,X,Y;

int main(){
	cin >> N >> M >> X >> Y;
	int x[N],y[M];
	int maxx=-100, miny=100;
	for(int i=0;i<N;i++){
		cin >> x[i];
		if(maxx < x[i]) maxx=x[i];
	}
	for(int i=0;i<M;i++){
		cin >> y[i];
		if(miny > y[i]) miny=y[i];
	}
	if(maxx  < miny) cout << "No War" << endl;
	else cout << "War" << endl;
	return 0;
}
