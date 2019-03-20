#include <bits/stdc++.h>
using namespace std;



int main(){
	int n,q;scanf("%d", &n);
	int a[n];
	for(int i=0;i<n;i++){
		scanf("%d", &a[i]);// cin >> ;
	}
	cin >> q;
	int b[q];
	int ans=0;
	for(int i=0;i<q;i++){
		scanf("%d", &b[i]);// cin >> b[i];
		int l=0,r=n;
		while(l<r){
			int j=(l+r)/2;
			if(b[i] == a[j]){
				ans++;
				break;
			}else if(b[i] > a[j]){
				l = j + 1;
			}else if(b[i] < a[j]){
				r = j;
			}
		}
	}
	cout << ans << endl;

	return 0;
}
