#include <bits/stdc++.h>
#define N 100
#define INFTY (1<<21)

using namespace std;

int n, M[N][N];
int d[N];

void bfs(int s) {
	queue<int> q;
	q.push(s);
	for(int i=0; i<n;i++) d[i]= INFTY;
	d[s] = 0;
	int u;
	while( !q.empty()) {
		u = q.front(); q.pop();
		for (int v = 0; v < n; v++) {
			if (M[u][v] == 0) continue;
			if (d[v]!= INFTY) continue;
			d[v] = d[u] + 1;
			q.push(v);
		}
	}
	for(int i=0;i<n; i++) {
		cout << i+1 << " " << ( (d[i] == INFTY) ? (-1) : d[i] ) << endl;
	}
}

int main(){
	int u, k, v;
	cin >> n;
	for(int i=0; i<n;i++) {
		cin >> u >> k;
		u--;
		for (int j =0; j<k;j++) {
			cin >> v;
			v--;
			M[u][v] = 1;
		}
	}
	bfs(0);
	return 0;
}
