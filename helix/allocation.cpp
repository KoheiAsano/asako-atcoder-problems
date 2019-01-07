#include <bits/stdc++.h>
using namespace std;

#define MAX 100000
typedef long long ll;

int n,k;
ll T[MAX];

int check(ll P){// P =一台当たりの最大積載量
  int i = 0;//詰める荷物の数
  for (int j = 0; j < k; j++) {//j = Track の index
    ll s = 0;// 一台あたりにつめる荷物
    while( s + T[i] <= P ) {
      s += T[i];
      i++;
      if( i == n ) return n;
    }
  }
	return i;
}

int solve() {
  ll left = 0;
  ll right = 100000 * 10000;
  ll mid;
  while (right - left > 1) {
		// cout << "right = " << right << " left = " << left << endl;
    mid = (left + right) / 2;
		// cout << "mid = " << mid <<endl;
    int v = check(mid);// mid == １台あたりの最大積載量
		// cout << "v = " << v <<endl;
    if ( v == n) right = mid; // つみきれるなら最大積載量を減らす(ために右端を減らす)
    else left = mid;// つみきれないので増やす
  }
  return right;
}

int main() {
  cin >> n >> k;
  for (int i = 0;i < n; i++) cin >> T[i];
  ll ans = solve();
  cout << ans << endl;
	return 0;
}
