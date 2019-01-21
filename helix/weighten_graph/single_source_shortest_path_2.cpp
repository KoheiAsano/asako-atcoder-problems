#include <bits/stdc++.h>
using namespace std;
#define MAX 10000
#define INFTY (1<<20)
#define WHITE 0
#define GRAY 1
#define BLACK 2

int n;
vector<pair<int, int> > adj[MAX];

void dijkstra() {
  priority_queue<pair<int, int> > PQ;
  int d[MAX], color[MAX];
  for ( int i = 0; i < n; i ++) {
    d[i] = INFTY;
    color[i] = WHITE;
  }

  d[0] = 0;
  PQ.push(make_pair(0,0));
  color[0] = GRAY;
  while ( !PQ.empty() ) {
    pair<int, int> f = PQ.top(); PQ.pop();//(cost, Nodeid)
    int u = f.second;
    color[u] = BLACK;
    if( d[u] < f.first * ( -1 ))continue;//今の最小Nodeよりコストが大きいなら再計算はしない
    for (int j = 0; j < adj[u].size(); j++) {
      int v = adj[u][j].first;
      if (color[v] == BLACK) continue;
      if (d[v] > d[u] + adj[u][j].second) {
        d[v] = d[u] + adj[u][j].second;
        PQ.push(make_pair(d[v] * (-1), v));//STL priority_queueはmaximum
        color[v] = GRAY;
      }
    }
  }
  for (int i =0; i< n; i++) {
    cout << i << " " << ( d[i] == INFTY ? -1 : d[i]) << endl;
  }
}

int main(){

  int k, c, u, v;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> u >> k;
    for (int j = 0; j<k;j++) {
      cin >> v >> c;
      adj[u].push_back(make_pair(v,c));
    }
  }
  dijkstra();

  return 0;
}
