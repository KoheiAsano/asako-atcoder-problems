#include <bits/stdc++.h>
using namespace std;

#define ll long long

int N;
int A[1001];
int main(){
	cin >> N;
	for(int i=0;i<N;i++){
		cin >> A[i];
	}
	int minans = 2000000000;

	for(int i=-100;i<101;i++){
		int candi = 0;
		for(int j=0;j<N;j++){
			candi+=(A[j]-i)*(A[j]-i);
		}
		minans = min(minans,candi);
	}
	cout << minans << endl;
	return 0;
}
