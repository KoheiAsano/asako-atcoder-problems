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
    int seqcount = 0;
		for(int j=i+1;j<N;j++){
			if(p<a[j]){
        seqcount++;
				cout << "(" << i << j << ")" << endl;
				ans+=seqcount;
				p = a[j];
			}
			else break;
		}
    i += seqcount;
	}
	cout << ans << endl;
	return 0;
}
// 6
// 1 2 3 2 1 2
// 5
// 1 2 3 1 2
