#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
using namespace std;


int W,H;
ll memo[10006][10006]={0};


int main(){
	cin >> W >> H;
	for(int i=0;i<W;i++)memo[i][0]=1;
	for(int i=0;i<H;i++)memo[0][i]=1;
	for(int i=1;i<H;i++){
		for(int j=1;j<W;j++){
			memo[j][i] = memo[j-1][i] + memo[j][i-1] ;
			memo[j][i]%= MOD;
		}
	}

	cout << memo[W-1][H-1] << endl;
	return 0;
}
