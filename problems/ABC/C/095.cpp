#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000

int A,B,C;

int X,Y;

int main(){
	cin >> A >> B >> C >> X >> Y;
	int AB=2*C;
	int ans=0;
	int dif = X-Y;
	if(A + B < AB){
		ans += A*X + B*Y;
	}else{// if(A + B >= AB)
		ans += min(X,Y)*AB;
		if(dif > 0){
			if(A < AB){
				ans += dif*A;
			}else{
				ans += dif*AB;
			}
		}else if(dif < 0){
			if(B < AB){
				ans += -dif*B;
			}else{
				ans += -dif*AB;
			}
		}
	}
	cout << ans << endl;
	return 0;
}
