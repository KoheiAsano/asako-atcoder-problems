#include <bits/stdc++.h>
using namespace std;




int main(){
	int N; cin >> N;
	int a[N];
	int ans =0;
	for(int i=0;i<N;i++){
		cin >> a[i];
		ans ++;
	}

	for(int i=0;i<N;i++){
		int p = a[i];
		for(int j=i+1;j<N;j++){
			if(p<a[j]){
				// cout << "(" << i << j << ")" << endl;
				ans++;
				p = a[j];
			}
			else break;
		}
	}
	cout << ans << endl;
	return 0;
}
