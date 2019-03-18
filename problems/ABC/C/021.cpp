#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define mod 1000000007
int n,a,b,m,x,y,d[111][111];
vector<int>v[111];
signed main(){
	cin>>n>>a>>b>>m;
	a--,b--;
	d[0][a]=1;//始点への経路は１
	while(m--){
		cin>>x>>y;
		v[x-1].push_back(y-1);
		v[y-1].push_back(x-1);
	}
	// for(int i=0;i<n;i++){
	// 	for(int k=0;k<v[i].size();k++){
	// 		cout << v[i][k] << " ";
	// 	}
	// 	cout <<endl;
	// }
	for(int i=0;i<111;i++){
		for(int j=0;j<n;j++){
			if(d[i][j]==0)continue;//始点でも始点からつながった点でもないものは無視
			if(j==b){
				// for(int l = 0;l<=i;l++){
				// 	for(int m = a;m<=j;m++){
				// 		cout << d[l][m] << " ";
				// 	}
				// 	cout << endl;
				// }
				cout<<d[i][j]<<endl;
				return 0;
			}
			for(int k=0;k<v[j].size();k++){// Node jからのびるやつらに、そこまでの経路を加算する
				d[i+1][v[j][k]]+=d[i][j];
				d[i+1][v[j][k]]%=mod;
			}
		}
	}
	return 0;
}
