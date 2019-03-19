#include <bits/stdc++.h>
using namespace std;

int A,B,C;

bool ao=true,bo=true,co=true;


int main(){
  cin >> A >> B >> C;
  if(A%2 == 0) ao = false;
  if(B%2 == 0) bo = false;
  if(C%2 == 0) co = false;
  int ans = 0;
	if(!((ao && bo && co) || (!ao && !bo && !co))) {
		if(ao != bo && bo == co){
			B++;C++;
		}
		else if(co != bo && bo == ao){
			B++;A++;
		}
		else if(bo != ao && ao == co){
			A++;C++;
		}
		ans++;
	}
	int maxi = max(A,B);
	maxi = max(maxi,C);
  ans += (maxi-A)/2 + (maxi-B)/2 + (maxi-C)/2;
	cout << ans << endl;
	return 0;
}
