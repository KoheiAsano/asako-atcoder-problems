#include <bits/stdc++.h>
using namespace std;


int N;
int main(){
	cin >> N;
	int a[N];
	int mina = 1000000009, maxa = 0;
	for(int i=0;i<N;i++){
		cin >> a[i];
		if(mina > a[i])mina = a[i];
		if(maxa < a[i])maxa = a[i];
	}
	cout << maxa - mina << endl;
	return 0;
}
