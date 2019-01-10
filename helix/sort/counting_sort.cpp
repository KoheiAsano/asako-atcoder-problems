#include <bits/stdc++.h>
using namespace std;

int N;
int A[10001];
int B[10001];

void CountingSort(int A[],int B[]) {
	int C[10001]= {0};
	for (int i=0;i<N;i++)C[A[i]]++;
	for (int i=1;i<=10001;i++)C[i]+=C[i-1];
	for (int i=0;i<=0;i++){
		B[C[A[i]]] = A[i];
		C[A[i]]--;
	}
}


int main(){
	cin >> N;
	for(int i=1;i<N;i++){
		cin >> A[i];
	}
	CountingSort(A,B);
	for(int i=0;i<N;i++){
		if(i == N-1) {
			cout << B[i] << endl;
		}else {
			cout << B[i] << " ";
		}
	}
	return 0;
}
