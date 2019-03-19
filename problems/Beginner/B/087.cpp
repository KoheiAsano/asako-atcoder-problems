#include <bits/stdc++.h>
using namespace std;
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))

int A,B,C;
int X;
int main(){
	cin >> A >> B >> C >> X;
	int ans=0, rest;
	for(int i=0;i<=A;i++){
		for(int j=0;j<=B;j++){
			rest = X - i*500 - j*100;
			if(rest <= C*50 && rest >= 0)ans ++;
		}
	}
	cout << ans << endl;
	return 0;
}
