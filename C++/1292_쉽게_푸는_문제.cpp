#include <iostream>
#include <stdio.h>
using namespace std;

int solved_1292_쉽게_푸는_문제() {
	int a, b;
	scanf("%d %d", &a, &b);

	int tmp = 1;
	int cnt = 1;
	int sum = 0;
	for (int i = 0; i < b; i++) {

		if (cnt == 0) {
			tmp++;
			cnt = tmp;
		}

		if (i >= (a - 1)) {
			sum += tmp;
		}
		cnt--;
		printf("tmp : %d / cnt : %d\n", tmp, cnt);
	}

	printf("sum : %d\n", sum);
	system("pause");
	return 0;
}