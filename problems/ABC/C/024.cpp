#include <bits/stdc++.h>
using namespace std;

int N, D, K;
int L[10006],R[10006],S[109],T[109];

int main(){
	cin >> N >> D >> K;
	for(int i=0;i<D;i++){
		cin >> L[i] >> R[i];
	}
	int d[K];
	for(int i=0;i<K;i++){
		cin >> S[i] >> T[i];
		if(S[i] < T[i]){
			for(int j=0;j<D;j++){
				if(R[j] >= S[i] && S[i] >= L[j])S[i]=R[j];//Sを現在地に利用。移動できるならできるだけする
				if(S[i] >= T[i]){
					d[i]=j+1;//ゴールできる日
					break;
				}
			}
		}
		else{
			for(int j=0;j<D;j++){
				if(L[j] <= S[i] && S[i] <= R[j]){
					S[i]=L[j];//Sを現在地に利用。移動できるならできるだけする
				}
				if(S[i] <= T[i]){
					d[i]=j+1;//ゴールできる日
					break;
				}
			}
		}
	}
	for(int i=0;i<K;i++){
		cout << d[i] << endl;
	}
	return 0;
	// for(int i=0;i<D;i++){
	// 	cout << L[i] <<" " << R[i] << endl;
	// }
	// cout << endl;
	// for(int i=0;i<K;i++){
	// 	cout << S[i] << " " << T[i] << endl;
	// }
}
