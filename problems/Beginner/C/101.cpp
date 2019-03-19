#include <bits/stdc++.h>
using namespace std;



int main(){
	int N,K;cin >> N >> K;
  int A0[N];
	vector<int> V0, V1;
	int fc=0, bc=0;
	int tmp;
  //1で配列をSplitする。その時1は複製する
	for(int i=0;i<N;i++){
		cin >> A0[i];
		fc++;
		tmp = i;
		if(A0[i] ==1) break;
	}

	//１の分をIncrementしてから残りも数える。
	bc++;
	for(int i=tmp+1;i<N;i++){
		cin >> A0[i];
		bc++;
	}

	int ans =0;
	//前の計算
	// cout << fc << endl;
	// if(fc > 1){
	// 	ans++;
	// 	fc -=K;
	// 	while(fc>0){
	// 		fc-=K-1;
	// 		ans++;
	// 	}
	// }
	// cout << ans << endl;
	//後ろの計算
	// if(bc > 1){
	// 	ans++;
	// 	bc -=K;
	// 	while(bc>0){
	// 		bc-=K-1;
	// 		ans++;
	// 	}
	// }
	ans = (N-1)/(K-1);
	if((N-1)%(K-1) != 0)ans++;
	cout << ans << endl;
  return 0;
  // そしたら二つの配列の長さをa0.a1,としたら
  // a0/N + a1/N わりきれない場合はインクリメント

}
