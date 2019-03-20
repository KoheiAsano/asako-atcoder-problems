#include <bits/stdc++.h>
using namespace std;

stack<int> S;
int a, b, x;
string s;

int main(){
	while(cin >> s) {
		if(s[0] == '+'){
			a = S.top();S.pop();
			b = S.top();S.pop();
			S.push(a+b);
		}else if(s[0] == '-'){
			b = S.top();S.pop();
			a = S.top();S.pop();
			S.push(a-b);
		}else if(s[0] == '*'){
			a = S.top();S.pop();
			b = S.top();S.pop();
			S.push(a*b);
		}else{
			S.push(atoi(s.c_str()));
		}
	}
	cout << S.top() << endl;
	return 0;
}
