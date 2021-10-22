#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

#define N_MAX 101

int region[N_MAX][N_MAX];
bool visited[N_MAX][N_MAX] = { false, };
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
int min_v = N_MAX, max_v = 0;
queue<pair<int, int>> q;

int dfs(int n, int water_lv) {
	memset(visited, false, sizeof(visited));
	int x = 0, y = 0, nx = 0, ny = 0;
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (region[i][j] >= water_lv && !visited[i][j]) {
				q.push(make_pair(i, j));
				visited[i][j] = true;
				while (!q.empty()) {
					x = q.front().first;
					y = q.front().second;
					q.pop();

					for (int d = 0; d < 4; d++) {
						nx = x + dx[d];
						ny = y + dy[d];
						if (nx >= n || ny >= n || nx < 0 || ny < 0) continue;
						if (region[nx][ny] >= water_lv && !visited[nx][ny]) {
							q.push(make_pair(nx, ny));
							visited[nx][ny] = true;
						}
					}
				}
				cnt++;
			}
		}
	}
	return cnt;
}
int solved_2468() {
	ios_base::sync_with_stdio(false);  // 처리속도 ++
	cin.tie(NULL);

	int n;
	int result = 1;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> region[i][j];
			min_v = min(min_v, region[i][j]);
			max_v = max(max_v, region[i][j]);
		}
	}
	for (int i = min_v; i < max_v; i++) {
		result = max(result, dfs(n, i));
	}
	cout << result << endl;
	system("pause");
	return 0;
}