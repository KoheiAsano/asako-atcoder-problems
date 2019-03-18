#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;

char field[4][4];

int main(){
	for (int i =0;i<4;i++){
		for (int j =0;j<4;j++){
			cin >> field[i][j];
		}
	}
	for (int i =3;i>=0;i--){
		for (int j =3;j>=0;j--){
			cout << field[i][j];
			if(j) cout << " ";
		}
		cout << endl;
	}
	return 0;
}
