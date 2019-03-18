#include <bits/stdc++.h>
using namespace std;



int main(){
	int N;cin >> N;
	int a[N];
	int maxsum =0;
	for(int i=0;i<N;i++){
		cin >> a[i];
		maxsum+=a[i] -1;
	}
	cout << maxsum << endl;
	return 0;
}
