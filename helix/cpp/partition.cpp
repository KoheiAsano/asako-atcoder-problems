#include <bits/stdc++.h>
using namespace std;

int N;
int A[100006];
void swap(int& a, int& b){
	int tmp = a;
	a = b;
	b = tmp;
}

int partition(int p, int r) {
	int x = A[r];
	int i = p-1;
	for(int j = p;j<r;j++){
		if(A[j] <= x) {
			i++;
			swap(A[i], A[j]);
		}
	}
	swap(A[i+1], A[r]);
	return i+1;
}


int main(){
	cin >> N;
	for(int i=0;i<N;i++)cin >> A[i];
	int cu = partition(0,N-1);
	for(int i=0;i<N;i++){
		if(i)cout << " ";
		if(i == cu)cout << "[";
		cout << A[i];
		if(i == cu)cout << "]";
	}
	cout << endl;
	return 0;
}
