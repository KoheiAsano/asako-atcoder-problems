#include <bits/stdc++.h>
using namespace std;

#define FOR(i,s,e) for(int i=s;i<e;i++)
#define RFOR(i,s,e) for(int i=s;i>=e;i--)

#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))

#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))
#define MAX(arr) *max_element(arr, arr + ARRAY_LENGTH(arr))
#define MAXID(arr) distance(arr,max_element(arr, arr + ARRAY_LENGTH(arr)))
#define MIN(arr) *min_element(arr, arr + ARRAY_LENGTH(arr))
#define MINID(arr) distance(arr,min_element(arr, arr + ARRAY_LENGTH(arr)))
#define NID(arr,x) distance(arr,find(arr, arr + ARRAY_LENGTH(arr),x))

#define INF 1000000000
#define EPS (1e-7)

int R,C;
int sx,sy;
int gx,gy;
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
char c[51][51];

int d[51][51];

typedef pair<int, int> P;

int main(){
	cin >> R >> C;
	cin >> sy >> sx;
	sy--;sx--;
	cin >> gy >> gx;
	gy--;gx--;
	// cout << sx << sy << gx << gy << endl;
	FOR(i,0,R){
		FOR(j,0,C){
			cin >> c[j][i];
		}
	}
	FOR(i,0,R){
		FOR(j,0,C){
			d[j][i] = INF;
		}
	}

	queue<P> que;
	que.push(P(sx,sy));
	d[sx][sy] = 0;

	while(que.size()) {
		P p = que.front(); que.pop();

		if (p.first == gx && p.second == gy) break;

		for(int i = 0; i<4;i++){
			int nx = p.first + dx[i], ny = p.second + dy[i];
      //フィールド内＾壁でない^行ったことがない
			if(0<=nx && nx <C && 0<=ny && ny < R && c[nx][ny] != '#' && d[nx][ny] == INF){
				que.push(P(nx,ny));
				d[nx][ny] = d[p.first][p.second] + 1;
			}
		}
	}
	cout << d[gx][gy] << endl;
	return 0;
}

/*input
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
*/

/*output
11
*/
