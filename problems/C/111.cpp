#include <bits/stdc++.h>
using namespace std;
#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))
#define MAX(arr) *max_element(arr, arr + ARRAY_LENGTH(arr))
#define MAXID(arr) distance(arr,max_element(arr, arr + ARRAY_LENGTH(arr)))

int N;
int ev[10006], ov[10006];
int ob[10006]={0}, eb[10006]={0};
int ans, omost, emost, otmp, etmp;
int main(){
	cin >> N;

	for(int i=0;i<N;i++){
		if(i%2==0){
			cin >> ev[i];
			eb[ev[i]]++;
		}
		else {
			cin >> ov[i];
			ob[ov[i]]++;
		}
	}
	omost= MAXID(ob);
	emost= MAXID(eb);
	if (omost!=emost){
		ans = N-MAX(ob)-MAX(eb);
		cout << N-MAX(ob)-MAX(eb) << endl;
	}
	else{
		otmp = MAX(ob);
		etmp = MAX(eb);
		ob[omost]=0;eb[emost]=0;
		ans = min(N-MAX(ob)-etmp,N-MAX(eb)-otmp);
		cout << ans << endl;
	}
	return 0;
}
