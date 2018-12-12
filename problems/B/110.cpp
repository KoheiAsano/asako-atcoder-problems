#include <bits/stdc++.h>
using namespace std;


int N,M,X,Y;

int main(){
	cin >> N >> M >> X >> Y;
	int x[N+1],y[M+1];
	int maxx=X, miny=Y;
	for(int i=0;i<N;i++){
		cin >> x[i];
		if(maxx < x[i]) maxx=x[i];
	}
	for(int i=0;i<M;i++){
		cin >> y[i];
		if(miny > y[i]) miny=y[i];
	}

	if(maxx+1 < miny) cout << "No War" << endl;
	else cout << "War" << endl;
	return 0;
}
