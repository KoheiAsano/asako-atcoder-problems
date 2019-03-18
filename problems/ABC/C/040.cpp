#include <bits/stdc++.h>
#define INF 999999999
using namespace std;


int N;
int dp[100006]={0};
int main(){
	cin >> N;
	int a[N];
	for(int i=0;i<N;i++)cin >> a[i];
	for(int i=1;i<=N+5;i++){
		dp[i] = INF;
	}
	for(int i=0;i<N;i++){
		dp[i+1] = min(dp[i + 1], dp[i] + (abs(a[i+1]-a[i])));
		dp[i+2] = min(dp[i +2], dp[i] + (abs(a[i+2]-a[i])));
	}
	// for(int i=0;i<N;i++){
	// 	cout << dp[i] << endl;
	// }
	cout << dp[N-1] << endl;
	return 0;
}
