#include <bits/stdc++.h>
using namespace std;


int N;

int main(){
	cin >> N;
	int x[N], y[N], h[N];
	int maxh = 0;
	for(int i=0;i<N;i++){
		cin >> x[i] >> y[i] >> h[i];
	}
	for(int cx=0;cx<101;cx++){
		for(int cy=0;cy<101;cy++){
			for(int k=0;k<N;k++){
				int ch = abs(x[k]-cx)+ abs(y[k]-cy) + h[k];
				for(int l=0;l<N;l++){
					if(max(ch-abs(x[l]-cx)-abs(y[l]-cy),0) != h[l]){
						break;
					}else if(l == N-1){
						cout << cx << " " << cy << " " << ch << endl;
						return 0;
					}　
				}
			}
		}
	}
	return 0;
}
