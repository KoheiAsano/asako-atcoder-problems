#include <bits/stdc++.h>
using namespace std;


int N;

int main(){
	cin >> N;
	int M[100][100]={0};
	int t,a,k;
	for(int i=0;i<N;i++){
		cin >> t >> k;
		t--;
		for(int j=0;j<k;j++){
			cin >> a;
			a--;
			M[t][a] = 1;
		}
	}
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if (j) cout << " ";
			cout << M[i][j];
		}
		cout << endl;
	}
}
