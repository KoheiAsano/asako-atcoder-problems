#include <bits/stdc++.h>
using namespace std;

// 5000,0000,0000,0000
int N, K;

int main(){
	cin >> N >> K;
	long long k=0;
	long long rk2=0;
	if(K%2 == 0){
		for(int i=1;i<=N;i++){
			if(i%K == 0)k++;
			else if(i%K == K/2) rk2++;
		}
	}else{
		for(int i=1;i<=N;i++){
			if(i%K == 0)k++;
		}
	}
	cout << k*k*k + rk2*rk2*rk2 << endl;
	return 0;
}
