#include <iostream>
#include <utility>
#include <queue>
#define debug(x) cerr << #x << ": " << x << endl;
using namespace std;
static const int INF=1000000000;

int N,M;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
queue<pair<int, int> > Q;

char map[1000][1000];
int dis[1000][1000] = {INF};
int main(){
	cin >> N >> M;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			cin >> map[i][j];
			if (map[i][j] == '#'){
				Q.push(make_pair(i,j));
				dis[i][j] = 0;
			}
		}
	}
	int tx,ty, ans=0;
	while(!Q.empty()){
		pair<int, int> p = Q.front();Q.pop();
		for (int i=0;i<4;i++){
			tx = p.first + dx[i];
			ty = p.second + dy[i];
			if(0 <= tx && tx <= N-1 && 0 <= ty && ty <= M-1 && map[tx][ty] == '.'){
				map[tx][ty] = '#';
				dis[tx][ty] = dis[p.first][p.second] + 1;
				ans = max(ans, dis[tx][ty]);
				Q.push(make_pair(tx,ty));
			}
		}
	}
	cout << ans << endl;
}
