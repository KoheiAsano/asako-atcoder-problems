#include <bits/stdc++.h>
using namespace std;


int H, W;

int main(){
	cin >> H >> W;
	char C[H+1][W+1];
	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			cin >> C[i][j];
		}
	}
	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			cout << C[i][j] ;
		}
		cout << endl;
		for(int j=0;j<W;j++){
			cout << C[i][j];
		}
		cout << endl;
	}
	return 0;
}
