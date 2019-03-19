#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;



int main(){
	cin >> n;
	int T[n];
	int mini = 9999999;
	for (int i =0;i<n;i++){
		cin >> T[i];
		mini = min(T[i],mini);
	}
	cout << mini << endl;
}
