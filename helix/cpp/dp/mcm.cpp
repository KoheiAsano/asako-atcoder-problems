#include <bits/stdc++.h>
using namespace std;


int n;
int p[102], m[102][102]={0};// i, j間のコスト
int main(){
	cin >> n;
	for(int i=1;i<=n;i++){
		cin >> p[i-1] >> p[i];
	}
	for( int l = 2; l <= n; l++) {//行列の積の数
		for (int i = 1; i<= n - l + 1;i++) {
			int j = i + l - 1;//iに対してl離れた行列のIndex
			m[i][j] = (1 << 21);
			for (int k = i; k<= j - 1; k++) {//積の分割点=k
				m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i - 1] * p[k] * p[j]);
			}
		}
	}
	cout << m[1][n] << endl;
	return 0;
}
