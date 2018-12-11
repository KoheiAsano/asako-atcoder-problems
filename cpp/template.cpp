#include <bits/stdc++.h>
using namespace std;

#define FOR(i,s,e) for(int i=s;i<e;i++)
#define RFOR(i,s,e) for(int i=s;i>=e;i--)

#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))

#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))
#define MAX(arr) *max_element(arr, arr + ARRAY_LENGTH(arr))
#define MAXID(arr) distance(arr,max_element(arr, arr + ARRAY_LENGTH(arr)))
#define MIN(arr) *min_element(arr, arr + ARRAY_LENGTH(arr))
#define MINID(arr) distance(arr,min_element(arr, arr + ARRAY_LENGTH(arr)))
#define NID(arr,x) distance(arr,find(arr, arr + ARRAY_LENGTH(arr),x))

#define INF 1000000000
#define EPS (1e-7)

double N;
double ans=0;


int main(){
	cin >> N;
	FOR(i,1,N+1){
		ans+=i*10000/N;
	};
	cout << ans << endl;
	return 0;
}
