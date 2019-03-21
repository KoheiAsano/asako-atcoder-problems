#include <bits/stdc++.h>
using namespace std;


int H;

int A[500006];

int parent(int i){return i/2;};
int right(int i){return 2*i + 1;};
int left(int i){return 2*i;};

void swap(int& a, int& b){
	int tmp = a;
	a = b;
	b = tmp;
}


void maxHeapify(int A[],int i) {
	int l = left(i), r = right(i);
	int maximum;
	if(l <=H && A[l] > A[i]) maximum = l;
	else maximum = i;
	if(r <=H && A[r] > A[maximum]) maximum = r;
	if(maximum != i){
		swap(A[maximum], A[i]);
		maxHeapify(A,maximum);
	}
}

void buildMaxHeap(int A[]) {
	for(int i = H/2;i>0;i--){
		maxHeapify(A,i);
	}
}

int main(){
	cin >> H;
	for(int i=1;i<=H;i++)cin >> A[i];
	buildMaxHeap(A);
	for(int i=1;i<=H;i++){
		cout << " " << A[i];
	}
	cout << endl;
	return 0;
}
