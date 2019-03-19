#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000

int X;

int main(){
	cin >> X;
	int ans =1;
	for(int i=2;i < sqrt(X);i++){
		int n=2;
		while(pow(i,n) <=X){
			int tmp = pow(i,n);
			ans = max(tmp,ans);
			n++;
		}
	}
	cout << ans << endl;
	return 0;
}
