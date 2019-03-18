#include <bits/stdc++.h>
using namespace std;


int D, N;
int t,ta;
int main(){
	cin >> D >> N;
	if (D == 0) t = 1;
	else t = pow(100,D);
	if(N != 100){
		cout << t * N << endl;
	}else{
		cout << t * (N+1)  << endl;
	}
	return 0;
}
