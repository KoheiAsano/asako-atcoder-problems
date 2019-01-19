#include <bits/stdc++.h>
using namespace std;

int a[500][500];

int main()
{
  int r, c, k;
  cin >> r >> c >> k;

  string s[500];
  for(int i = 0; i < r; i++){
    cin >> s[i];
  }

  for(int i = 0; i < r; i++){
    for(int j = 0; j < c; j++){
      int cnt;
      for(cnt = 0; cnt <= k; cnt++){
        if(j-cnt < 0 or j+cnt >= c) break;
        if(s[i][j+cnt] == 'x' or s[i][j-cnt] == 'x') break;
      }
      a[i][j] = cnt;
    }
  }

  int ans = 0;
  k--;
  for(int i = k; i < r-k; i++){
    for(int j = k; j < c-k; j++){
      bool flag = true;
      for(int l = -k; l <= k; l++){
        if(a[i+l][j] < k-abs(l)+1){
          flag = false;
        }
      }
      if(flag){
        ans++;
      }
    }
  }

  cout << ans << endl;

  return 0;
}
