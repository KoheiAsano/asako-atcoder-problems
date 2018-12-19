#include <bits/stdc++.h>


#define FOR(i,s,e) for(int i=s;i<e;i++)
#define RFOR(i,s,e) for(int i=s;i>=e;i--)
#define INF 1000000000
#define EPS (1e-7)



#define ll long long
using namespace std;
typedef pair<int, int> P;
typedef pair<ll,ll> LP;

double N;
double ans=0;
const int INF = 2000000000;

int main(){
	cin >> N;
	FOR(i,1,N+1){
		ans+=i*10000/N;
	};
	cout << ans << endl;
	return 0;
}
