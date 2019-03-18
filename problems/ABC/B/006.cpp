#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 10007;
int n;

ll tri[1000001]={0};

int main(){
	cin >> n;
	tri[0] = 0;
	tri[1] = 0;
	tri[2] = 1;
	for (int i=3;i<n;i++){
		tri[i] = tri[i-1] + tri[i-2] + tri[i-3];
		tri[i] %= MOD;
	}
	cout << tri[n-1] << endl;
	return 0;
}
