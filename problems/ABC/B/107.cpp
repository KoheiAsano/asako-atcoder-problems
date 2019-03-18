#include <bits/stdc++.h>
using namespace std;


int H,W;

int main(){
	cin >> H >> W;
	int row[101]={0};
	int col[101]={0};
	char field[W][H];
	// fieldにいれながら判定
	for(int i=0;i<H;i++){
		for (int j=0;j<W;j++){
			cin >> field[j][i];
			if(field[j][i] == '#') {
				row[i]=1;
				col[j]=1;
			}
		}
	}
	// どっちもひっかからなかったIndexのみ出力
	for(int i=0;i<H;i++){
		if(row[i] == 1){
			for (int j=0;j<W;j++){
				if(col[j] == 1)cout << field[j][i];
			}
			cout << endl;
		}
	}
	return 0;
}
