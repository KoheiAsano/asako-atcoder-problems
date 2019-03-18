#include <bits/stdc++.h>
using namespace std;
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))

int N,Q;
int main(){
	cin >> N >> Q;
	int l[Q], r[Q];
	int field[200006]={0};
	for(int i=0;i<Q;i++){
		cin >> l[i] >> r[i];
		l[i]--;
	}
	for(int i=0;i<Q;i++){
		field[l[i]]++;field[r[i]]++;
	}
	bool flag = false;
	for(int i=0;i<N;i++){
		if(field[i]%2 == 1)flag = !flag;
		if(flag)cout << 1;
		else cout << 0;
	}
	cout << endl;
}
