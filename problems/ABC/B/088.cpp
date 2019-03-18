#include <bits/stdc++.h>
using namespace std;
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))

int N;
int main(){
	cin >> N;
	int a[N];
	for(int i=0;i<N;i++){
		cin >> a[i];
	}
	SORT(a);
	int bench;
	if(N%2 == 0)bench = 1;
	else bench = 0;
	int asum=0,bsum=0;
	for(int i=N-1;i>=0;i--){
		if(i%2 == bench) asum+=a[i];
		else bsum+=a[i];
	}
	cout << asum - bsum << endl;
	return 0;
}
