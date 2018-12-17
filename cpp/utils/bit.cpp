#include <bits/stdc++.h>
using namespace std;



int main(){
	int n; cin >> n;
	int a[n];
	for(int i=0;i<n;i++)cin >> a[i];
	int K; cin >> K;
	for(int bit = 0; bit < (1 << n); ++bit){
		vector<int> S;
		for( int i = 0; i < n; ++i){
			if (bit & (1 << i)) {
				S.push_back(i);
			}
		}

		int sum;
		for (int i=0;i< (int)S.size(); ++i) {
			sum += a[S[i]];
		}
		if(sum == K) {
			cout << "Yes" << endl;
			return 0;
		}
	}
	cout << "No" << endl;
	return 0;
}
