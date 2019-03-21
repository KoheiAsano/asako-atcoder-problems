#include <bits/stdc++.h>
using namespace std;




int main(){
	int N; cin >> N;
	int a[N];
	for(int i=0;i<N;i++){
		cin >> a[i];
	}
	for(int i=0;i<N;i++){
		for(int j=i;0<j;j--){
			if(a[j-1] > a[j]){
				int tmp = a[j-1];
				a[j-1] = a[j];
				a[j] = tmp;
			}else {
				break;
			}
		}
		for(int k=0;k<N;k++){
			if(k<N-1)cout << a[k] << " ";
			else cout << a[k] ;
		}
		cout << endl;
	}
	return 0;
}
