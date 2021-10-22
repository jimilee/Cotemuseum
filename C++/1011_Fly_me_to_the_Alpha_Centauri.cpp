#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int solved_1011() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		long long x, y;
		long long move, d = 0;
		scanf("%lld %lld", &x, &y);
		while (d*d <= y - x)
			d++;
		d--;
		move = 2 * d - 1;
		long long rem = y - x - (d * d);
		rem = (long long)ceil((double)rem / (double)d);
		move += rem;
		printf("%lld\n", move);
		cout << move << endl;
	}
	system("pause");
	return 0;
}