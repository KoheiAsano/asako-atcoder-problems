#include <bits/stdc++.h>
using namespace std;


int a, b;
int h[1001];
int num(int n){
	return n*(n+1)/2;
}

int main(){
	cin >> a >> b;
	h[1]=1;
	for(int i=2;i<1000;i++){
		h[i] = num(i);
		if(b-a==h[i]-h[i-1]) {
			cout << h[i] - b << endl;
			return 0;
		}
	}
	return 0;
}
