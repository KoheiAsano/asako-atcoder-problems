#include <bits/stdc++.h>
using namespace std;


int a1, b1, a2, b2;

int main(){
	cin >> a1 >> b1 >> a2 >> b2;
	int x =a2-a1;
	int y =b2-b1;
	cout << a2 - y << " " << b2 + x << " " << a1 - y << " " << b1 + x << endl;
	return 0;
}
