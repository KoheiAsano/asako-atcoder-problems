#include <bits/stdc++.h>
using namespace std;

int N, K;


int main(){
	cin >> N >> K;
	int ans =1;
	int count = N;
	while(ans<K && count > 0){
		ans*=2;
		count--;
	}
	while(count > 0){
		ans+=K;
		count--;
	}
	cout << ans << endl;
	return 0;
}
