#include <bits/stdc++.h>
using namespace std;

#define MAX 2000000
#define INFTY (1<<30)

int H, A[MAX+1];
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

int extract() {
	int maxv;
	if (H < 1) return -INFTY;
	maxv = A[1];
	A[1] = A[H--];
	maxHeapify(A,1);
	return maxv;
}

void increaseKey(int i, int key) {
	if(key < A[i]) return;
	A[i] = key;
	while( i > 1 && A[i/2] < A[i] ) {
		swap(A[i], A[i/2]);
		i/=2;
	}
}

void insert(int key) {
	H++;
	A[H] = -INFTY;
	increaseKey(H, key);
}

int main(){
	int key;
	char com[10];

	while (1) {
		scanf("%s", com);
		if( com[0] == 'e' && com[1] == 'n') break;
		if( com[0] == 'i') {
			scanf("%d", &key);
			insert(key);
		} else {
			printf("%d\n", extract());
		}
	}
	return 0;
}
