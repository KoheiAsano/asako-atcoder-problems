#include <bits/stdc++.h>
using namespace std;


int N;
int main(){
	cin >> N;
	int a[N];
	int ans;
	for(int i=0;i<N;i++){
		cin >> a[i];
		while(a[i] % 2 == 0){
			a[i] /=2;
			ans++;
		}
	}
	cout << ans << endl;
	return 0;
}
