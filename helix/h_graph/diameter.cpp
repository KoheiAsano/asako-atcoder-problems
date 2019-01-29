#include <bits/stdc++.h>
using namespace std;
static const int MAX = 100000;
static const int INFTY = (1<<30);

class Edge {//コンストラクタしかないただの構造体mdk
public:
  int t, w;
  Edge(){}
  Edge(int t, int w): t(t), w(w) {}
};

vector<Edge> G[MAX];//隣接リスト
int n, d[MAX];

bool vis[MAX];
int cnt;

void bfs(int s){
    for (int i = 0; i < n; i++) d[i] =INFTY;
    queue<int> Q;
    Q.push(s);
    d[s] = 0;
    int u;
    while( !Q.empty()) {
        u = Q.front(); Q.pop();
        for(int i =0; i < G[u].size(); i++) {//uに隣接するものでFor
            Edge e = G[u][i];
            if (d[e.t] == INFTY) {//未探索なら
                d[e.t] = d[u] + e.w;//現在のコスト＋u to eのコスト
                Q.push(e.t);
            }
        }
    }
}

void solve(){
    bfs(0);//0から最も遠いものを求める
    int maxv = 0;
    int tgt = 0;
    for (int i = 0; i < n; i++) {
        if (d[i] == INFTY) continue;
        if(maxv < d[i]) {
            maxv = d[i];
            tgt = i;
        }
    }

    bfs(tgt);
    maxv = 0;
    for (int i =0; i < n; i++) {
        if ( d[i] == INFTY) continue;
        maxv = max(maxv, d[i]);
    }
    cout << maxv << endl;
}

int main() {
    int s, t, w;
    cin >> n;

    for (int i = 0; i< n-1; i++) {
        cin >> s >> t >> w;
        G[s].push_back(Edge(t, w));
        G[t].push_back(Edge(s, w));
    }
    solve();
}
