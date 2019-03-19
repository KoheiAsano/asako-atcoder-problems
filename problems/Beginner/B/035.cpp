#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string S;
ll T;

int main(){
	cin >> S;
	cin >> T;
	ll x=0;
	ll y=0;
	ll a=0;
	for (int i=0;i<S.size();i++){
		if(S[i] == 'U'){y+=1;}
		else if(S[i] == 'D'){y-=1;}
		else if(S[i] == 'L'){x+=1;}
		else if(S[i] == 'R'){x-=1;}
		else{a+=1;}
	}
	if(T == 1){
		cout << abs(x) + abs(y) + a << endl;
	}else{
		if(abs(x) + abs(y) - a > 0)cout << abs(x) + abs(y) - a << endl;
		else cout << S.size()%2 << endl;
	}
	return 0;
}
