#include <bits/stdc++.h>
using namespace std;


#define ll long long

ll cnt = 0;
void swap(int& a, int& b){
	int tmp = a;
	a = b;
	b = tmp;
}

void insertionSort(int A[], int n, int g) {
	for(int i=g;i<n;i++){
		int v = A[i];
		int j = i - g;
		// cout << "g=" << g << "i=" << i << "j=" << j << endl;
		while( j>= 0 && A[j] > v) {
			// cout << "g=" << g << "i=" << i << "j=" << j << endl;
			A[j + g] = A[j];
			j -= g;
			cnt++;
			// cout <<" cnt=" << cnt << endl;
		}
		A[j + g] = v;
	}
}

// void shellSort(int A[], int n, vector<int> G[]){
//
// }


int main(){
	int N; cin >> N;
	int a[N];
	vector<int> G;
	for(int i=0;i<N;i++){
		cin >> a[i];
	}
	int h = 1;
	while(h<=N){
		G.push_back(h);
		h = 3 * h + 1;
	}
	cout << G.size() << endl;
	for(int i=G.size()-1;i>=0;i--){
		cout << G[i];
		if(i) cout << " ";
	}
	cout << endl;
	for(int i = G.size()-1;i>=0;i--){
		insertionSort(a, N, G[i]);
	}
	cout << cnt << endl;
	for(int k=0;k<N;k++){
		cout << a[k] << endl;
	}
	return 0;
}
