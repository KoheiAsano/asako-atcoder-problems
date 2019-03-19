#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))
using namespace std;


int N;


int main(){
	cin >> N;
	int d[N];
	for(int i=0;i<N;i++)cin >> d[i];
	SORT(d);
	int ans = 1;
	for(int i=1;i<N;i++){
		if(d[i]>d[i-1])ans++;
	}
	cout << ans << endl;
	return 0;
}
