#include <bits/stdc++.h>
using namespace std;

#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))

int N,X;


int gcd(int a, int b){
  if(a<b){
    int tmp = a;
    a = b;
    b = tmp;
  }
  int r=999;
  while(r!=0){
    r = a%b;
    a = b;
    b = r;
  }
  return a;
}

int main(){
	cin >> N >> X;
	// cout << gcd(N,X) << endl;
	int x[N+1];
	for(int i=0;i<N;i++){
		cin >> x[i];
	}
	x[N]=X;
	SORT(x);

	int ans=abs(x[0]-x[1]);
	for(int i=1;i<N;i++){
		ans = gcd(abs(x[i]-x[i+1]),ans);
	}
  cout << ans << endl;
	return 0;
}
