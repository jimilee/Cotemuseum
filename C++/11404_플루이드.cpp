#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

#define INF 99999999
#define N_MAX_SIZE 101

int cost[N_MAX_SIZE][N_MAX_SIZE];
int n, m;
int a, b, c;

void floyd() {
	for (int i = 1; i <= n; i++) { // i 지점 거칠 경우
		for (int j = 1; j <= n; j++) { // j 출발
			for (int k = 1; k <= n; k++) { // k도착
				if (cost[j][i] != INF && cost[i][k] != INF) {
					cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k]);
				}
			}
		}
	}
}
int solved_11404() {
	ios_base::sync_with_stdio(false);  // 처리속도 +++ / 92ms > 28ms
	cin.tie(NULL);

	cin >> n >> m;
	//scanf("%d", &n);
	//scanf("%d", &m);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cost[i][j] = INF;
		}
	}

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		if (cost[a][b] > c)
			cost[a][b] = c;
	}
	floyd();

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (i == j || cost[i][j] == INF)
				cout << 0 << " ";
			else
				cout << cost[i][j] << " ";
		}
		cout << endl;
	}

	system("pause");
	return 0;
}
