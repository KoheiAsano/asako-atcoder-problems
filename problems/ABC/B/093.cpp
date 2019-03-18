#include <bits/stdc++.h>
using namespace std;

int A, B, K;

void print(set<int> S) {
  for(set<int>::iterator it = S.begin(); it != S.end(); it++){
    cout << *it << endl;
  }
}

int main(){
	set<int> S;
	cin >> A >> B >> K;
	for (int i=0;i<K && i + A <= B;i++){
		S.insert(A + i);
	}
	for (int i=K-1;0<=i && B - i >= A;i--){
		S.insert(B - i);
	}
	print(S);
	return 0;
}
