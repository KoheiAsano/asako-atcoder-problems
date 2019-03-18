#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

map<string, int> T;
int main(){
	ll N;
	cin >> N;
	if(N%2 == 0){
		cout << N-1 << endl;
	}else{
		cout << N+1 << endl;
	}
	return 0;
}
