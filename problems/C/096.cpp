#include <bits/stdc++.h>
using namespace std;

int H,W;



int main(){
	cin >> H >> W;
	char s[H+2][W+2];
	// for(int i=0;i<W+2;i++){
	// 	s[0][i] = '.';
	// 	s[H+1][i] = '.';
	// }
	// for(int j=0;j<W+2;j++){
	// 	s[j][0] = '.';
	// 	s[j][W+1] = '.';
	// }
	for(int j=1;j<H+1;j++){
		for(int i=1;i<W+1;i++){
			cin >> s[j][i];
		}
	}
	for(int j=1;j<H+1;j++){
		for(int i=1;i<W+1;i++){
			if(s[j][i] == '#' && s[j][i+1] != '#' && s[j][i-1] != '#' && s[j+1][i] != '#' && s[j-1][i] != '#' ){
				cout << "No" << endl;
				return 0;
			}
		}
	}
	cout << "Yes" << endl;
	return 0;
}
