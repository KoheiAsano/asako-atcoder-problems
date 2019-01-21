#include <bits/stdc++.h>
using namespace std;
#define MAX 100
#define INFTY (1<<21)
#define WHITE 0
#define GRAY 1
#define BLACK 2
#define NIL -1

int n, M[MAX][MAX];

int prim() {
  int u, minv;
  int d[MAX], p[MAX], color[MAX];

  for (int i = 0; i < n; i++) {
    d[i] = INFTY;//各Nodeを連結しようとした時にかかる最小値(連結済みのNode依存)
    p[i] = -1;
    color[i] = WHITE;
  }

  d[0] = 0;

  while ( 1 ) {
    minv = INFTY;
    u = -1;
    for (int i =0; i<n; i++) {//次のステップで連結するNodeの決定
      if (minv > d[i] && color[i] != BLACK) {
        u = i;
        minv = d[i];
      }
    }
    if ( u == -1) break;
    color[u] = BLACK;//連結
    for (int v = 0; v < n; v++) {//連結したあとの、連結されてる点から、追加しようとした時の最小値をdに記録
      if ( color[v] != BLACK && M[u][v] != INFTY) {
        if (d[v] > M[u][v]) {
          d[v] = M[u][v];
          p[v] = u;//vと繋がったNodeをのちのために記録　
          color[v] = GRAY;
        }
      }
    }
  }
  int sum = 0;
  for (int i = 0; i < n; i++) {
    if (p[i] != -1) sum += M[i][p[i]];
  }

  return sum;
}

int main(){
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      int e; cin >> e;
      M[i][j] = (e == -1) ? INFTY : e;
    }
  }
  cout << prim() << endl;
  return 0;
}
