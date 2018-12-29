#include <bits/stdc++.h>
using namespace std;

queue<pair<string,int>> P;
int n,q,t;
string name;

int main(){
  cin >> n >> q;
  cout << n << q;
  for(int i = 0; i<n;i++){
    cin >> name >> t;
    P.push(make_pair(name, t));
  }
  pair<string, int> u;
  int elaps = 0, a;

  while(!P.empty()){
    u = P.front();P.pop();
    a = min(q,u.second);
    u.second-=a;
    elaps+=a;
    if(u.second>0){
      P.push(u);
    }else{
      cout << u.first << " " << elaps << endl;
    }
  }
	return 0;
}
