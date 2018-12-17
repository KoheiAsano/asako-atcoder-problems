#include <bits/stdc++.h>
using namespace std;




int main(){
	int n; cin >> n;
	int r[n];
	int maxdiff=-2147483647;

	for (int i=0;i<n;i++){
		cin >> r[i];
	}
	int minv=r[0];
	for (int i=1;i<n;i++){
		maxdiff = max(r[i]-minv,maxdiff);
		minv = min(minv,r[i]);
	}
	cout << maxdiff << endl;
	return 0;
}
