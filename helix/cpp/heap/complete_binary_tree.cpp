#include <bits/stdc++.h>
using namespace std;


int H;

int A[252];

int parent(int i){return i/2;};
int right(int i){return 2*i + 1;};
int left(int i){return 2*i;};

int main(){
	cin >> H;
	for(int i=0;i<H;i++)cin >> A[i];
	for(int i=0;i<H;i++){
		cout << "node " << i+1 << ": key = " << A[i] << ", ";
		if(parent(i+1)>0) cout << "parent key = " << A[parent(i+1)-1] << ", ";
		if(left(i+1)<H+1)cout <<  "left key = " << A[left(i+1)-1] << ", ";
		if(right(i+1)<H+1)cout <<  "right key = " << A[right(i+1)-1] << ", ";
		cout << endl;
	}
	return 0;
}
