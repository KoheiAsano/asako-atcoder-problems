#include <bits/stdc++.h>
using namespace std;
#define MAX 1000
#define VMAX 10000

int n, A[MAX], s;
int B[MAX], T[VMAX+1];

int solve() {
  int ans = 0;

  bool V[MAX];
  for( int i = 0; i < n; i ++ ) {
    B[i] = A[i];
    V[i] = false;
  }
  sort(B, B+n);
  for (int i = 0;i<n;i++)T[B[i]] = i;
  // for (int i = 0;i<n;i++)cout << A[i]<< " " << B[i]<< " "<< T[B[i]] << endl;
  for (int i =0;i < n; i ++) {
    if (V[i]) continue;
    int cur = i;
    int S = 0;
    int m = VMAX;
    int an = 0;//サイクルの要素数
    while (1) {
      V[cur] = true;
      an++;
      int v = A[cur];
      m = min(m,v);
      S += v;//サイクルのコストの総和
      cur = T[v];//上記で正しい順序のIndexバケツ？でサイクルができる
      if ( V[cur] ) break;
    }
    ans += min(S + (an - 2)*m, m+S + (an+1)*s);//左:サイクル内の最小値
  }
  return ans;
}

int main() {
  cin >> n;
  s = VMAX;
  for (int i = 0; i < n; i++) {
    cin >> A[i];
    s = min(s, A[i]);
  }
  int ans = solve();
  cout << ans << endl;
}
