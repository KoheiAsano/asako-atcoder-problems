#include <bits/stdc++.h>
#define INF 999999999
using namespace std;


int N;
int dp[100006]={0};

int f(int cu) {
	if (cu == 0) return 0;
	if(dp[cu]) return dp[cu];

	int res = INF;
	res = min(res, f(cu -1) + 1);

	int x = 6;
	while (x <=cu) {
		res = min(res, f(cu - x) + 1);
		x *= 6;
	}

	x = 9;
	while (x <=cu) {
		res = min(res, f(cu - x) + 1);
		x *= 9;
	}
	return dp[cu] = res;
}

int main(){
	cin >> N;
	cout << f(N) << endl;
	return 0;
}
