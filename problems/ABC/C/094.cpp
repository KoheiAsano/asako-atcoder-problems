#include <bits/stdc++.h>
using namespace std;
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))

#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))

int N;
int bucket[200001]={0};
int main(){
	cin >> N;
	int a[N],b[N];
	int mi=(N-1)/2;
	for (int i=0;i<N;i++){
		cin >> a[i];
		b[i] = a[i];
	}
	SORT(b);
	int md0=b[mi+1],md1=b[mi];

	for(int i=0;i<N;i++){
		if(a[i]<md0) cout << md0 << endl;
		else cout << md1 << endl;
	}

	return 0;
}
