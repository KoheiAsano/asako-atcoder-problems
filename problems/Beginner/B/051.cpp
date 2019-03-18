#include <bits/stdc++.h>
using namespace std;


int K,S;

int main(){
	cin >> K >> S;
	int k;
	int ans=0;
	for(int i=0;i<=K;i++){
		for(int j=0;j<=K;j++){
			k = S - i - j;
			if(k <=K && k>=0){
				ans++;
			}
		}
	}
	cout << ans << endl;
	return 0;
}
