#include <bits/stdc++.h>
using namespace std;


int N;
int bench[5]={105, 135,165,189,195};
int main(){
	cin >> N;
	if(N<bench[0]) {
		cout << 0 << endl;
		return 0;
	}
	else if (bench[0]<= N && N < bench[1]){
		cout << 1 << endl;
		return 0;
	}
	else if (bench[1]<= N && N <bench[2]){
		cout << 2 << endl;
		return 0;
	}
	else if (bench[2]<= N && N <bench[3]){
		cout << 3 << endl;
		return 0;
	}
	else if (bench[3]<= N && N <bench[4]){
		cout << 4 << endl;
		return 0;
	}
	else if (bench[4]<= N){
			cout << 5 << endl;
			return 0;
		}
}
