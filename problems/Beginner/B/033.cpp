#include <bits/stdc++.h>
using namespace std;


map<string, int> T;
int main(){
	int N;
	cin >> N;
	string name[N];
	int popu;
	int sum = 0;
	for (int i=0;i<N;i++){
		cin >> name[i] >> popu;
		sum +=popu;
		T.insert(make_pair(name[i], popu));
	}
	sum/=2;
	for (int i=0;i<N;i++){
		pair<string, int> target = *T.find(name[i]);
	  if(target.second > sum){
			cout << target.first << endl;
			return 0;
		}
	}
	cout << "atcoder" << endl;
	return 0;
}
