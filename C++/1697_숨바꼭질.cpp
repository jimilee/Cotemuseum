#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#define MAX 100001
using namespace std;
int n, k;

int solved_1697_¼û¹Ù²ÀÁú(int n, int k) {
	queue<pair<int, int>> que;
	bool visited[MAX] = {false};
	que.push(make_pair(n, 0));
	visited[n] = true;

	while (!que.empty()) {
		int d = que.front().first;
		int s = que.front().second;
		que.pop();
		printf("d - %d, s - %d\n", d, s);
		if (d == k) return s;

		if (d + 1 < MAX && !visited[d + 1]) {
			que.push(make_pair(d + 1, s + 1));
			visited[d + 1] = true;
		}
		if (d - 1 >= 0 && !visited[d - 1]) {
			que.push(make_pair(d - 1, s + 1));
			visited[d - 1] = true;
		}
		if (d * 2 < MAX && !visited[d * 2]) {
			que.push(make_pair(d * 2, s + 1));
			visited[d * 2] = true;
		}
	}
}

int main() {

	scanf("%d %d", &n, &k);

	printf("%d", move_n(n, k));

	system("pause");
	return 0;
}