#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll N,M;
int main(){
	cin >> N >> M;
	if(N == M){
		if(N == 1)cout << 1 << endl;
		else cout << (N-2)*(N-2) << endl;
	}
	else if(min(N,M) == 1) {
		cout << max(N,M)-2 << endl;
	}else{
		cout << (M-2)*(N-2) << endl;
	}
	return 0;
}
