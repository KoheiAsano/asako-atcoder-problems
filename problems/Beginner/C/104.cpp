#include <bits/stdc++.h>
using namespace std;

const int INF = 2000000000;

int main() {
  int D, G;cin >> D >> G;
  int p[D], c[D];
	for(int i = 0; i < D;i++){
		cin >> p[i] >> c[i];
	}
	//Bit全探索
	int minc = INF;
  for(int bit = 0; bit < (1 << D); ++bit){
		int count = 0;// 解く問題の個数
		int point = 0;//ポイント
		vector<int> S;// 解き切る問題のIndex
		int high;//中途半端に解く問題のIndex
		//解き切る問題のIndex集計
		for( int i = 0; i < D; ++i){
			if (bit & (1 << i)) {
				S.push_back(i);
			}else{
				high=i;
			}
		}
		//解き切る問題の計算
		for(int i=0;i<(int)S.size(); ++i){
			count += p[S[i]];
			point += p[S[i]]*(S[i]+1)*100 + c[S[i]];
		}

		for(int i=0;i<p[high] -1;i++){
			if(point < G){
				count ++;
				point+= (high+1)*100;
			}
		}
		if(point >= G) minc = min(minc, count);

  }
	cout << minc << endl;
	return 0;
}
