#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int N;


int main(){
	cin >> N;
	int ans = (1 << 29);
	for (int i=1;i<=sqrt(N);i++){
		int j = N/i;
		ans = min(ans, abs(j-i) + N-i*j);
	}
	cout << ans << endl;
}
