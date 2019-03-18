#include <iostream>
#include <map>
using namespace std;

int B[3][3],C[3][3],pow[10] = {1};
map<int,int> dp;

int code(int A[][3]){// 盤面に対して一意の整数を返す?
	int res = 0;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			res += A[i][j]*pow[i*3+j];
		}
	}
	return res;
}

bool end(int A[][3]){
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			if(A[i][j]==0) return false;
		}
	}
	return true;
}

int rec(int A[][3],int c){//A == 盤面、0 == NULL, 1 == o, 2 == x, c == 0 == 初手
	int num = code(A);
	// cout << num << endl;
	int score = 0,score1 = -1e9,score2 = 1e9;//そろっていたほうの得点
	if(dp.count(num)) return dp[num];
	if(end(A)){
		for(int i=0;i<2;i++){
			for(int j=0;j<3;j++){
				if(A[i][j]==A[i+1][j]) score += B[i][j];
			}
		}
		for(int i=0;i<3;i++){
			for(int j=0;j<2;j++){
				if(A[i][j]==A[i][j+1]) score += C[i][j];
			}
		}
		return score;
	}
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			if(A[i][j]==0){
				if(c==0){
					A[i][j] = 1;
					score1 = max(score1,rec(A,1));
					A[i][j] = 0;
				}else{
					A[i][j] = 2;
					score2 = min(score2,rec(A,0));
					A[i][j] = 0;
				}
			}
		}
	}
	if(c==0){
		dp[num] = score1;
		return score1;
	}
	else{
		dp[num] = score2;
		return score2;
	}
}

int main(){
	int sum = 0;
	for(int i=0;i<2;i++){
		for(int j=0;j<3;j++){
			cin >> B[i][j];
			sum += B[i][j];
		}
	}
	for(int i=0;i<3;i++){
		for(int j=0;j<2;j++){
			cin >> C[i][j];
			sum += C[i][j];
		}
	}
	for(int i=1;i<=9;i++) pow[i] = 3*pow[i-1];
	// for(int i=1;i<=9;i++) cout << pow[i] << endl;
	int A[3][3] = {};
	int ans = rec(A,0);
	cout << ans << endl;
	cout << sum-ans << endl;
}
