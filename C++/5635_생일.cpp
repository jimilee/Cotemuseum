#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int solved_5635_»ýÀÏ() {
	int n = 0;
	string most_old = "";
	int old_y = 9999, old_m = 99, old_d = 99;
	string most_young = "";
	int young_y = 0, young_m = 0, young_d = 0;

	scanf("%d", &n);
	string tmp = "";
	int tmp_y, tmp_m, tmp_d;

	for (int i = 0; i < n; i++) {
		cin >> tmp >> tmp_d >> tmp_m >> tmp_y;

		if (tmp_y < old_y) {
			old_y = tmp_y;
			old_m = tmp_m;
			old_d = tmp_d;
			most_old = tmp;
		}
		else if (tmp_m < old_m && tmp_y == old_y) {
			old_y = tmp_y;
			old_m = tmp_m;
			old_d = tmp_d;
			most_old = tmp;
		}
		else if (tmp_d < old_d && tmp_y == old_y && tmp_m == old_m) {
			old_y = tmp_y;
			old_m = tmp_m;
			old_d = tmp_d;
			most_old = tmp;
		}

		if (tmp_y > young_y ) {
			young_y = tmp_y;
			young_m = tmp_m;
			young_d = tmp_d;
			most_young = tmp;
		}
		else if (tmp_m > young_m && tmp_y == young_y) {
			young_y = tmp_y;
			young_m = tmp_m;
			young_d = tmp_d;
			most_young = tmp;
		}
		else if (tmp_d > young_d && tmp_y == young_y && tmp_m == young_m) {
			young_y = tmp_y;
			young_m = tmp_m;
			young_d = tmp_d;
			most_young = tmp;
		}

	}

	printf("%s\n", most_young.c_str());
	printf("%s\n", most_old.c_str());

	system("pause");
	return 0;
}