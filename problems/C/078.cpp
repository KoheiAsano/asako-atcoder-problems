#include <bits/stdc++.h>
using namespace std;

int N, M;

int main(){
	cin >> N >> M;
	int ans=1800*M + 100*N;
	ans*=pow(2,M);
	cout << ans << endl;
}
