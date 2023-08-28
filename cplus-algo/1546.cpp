#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	// 우선 최대값 M을 찾아야한다.
	// 그러기 위해선 우선 배열을 받아주고
	// 받는 순간 가장 큰 값을 찾아 M을 찾는다.

	// 이후 점수를 저장해둔 배열에서 값을 공식대로 수정해서 넣는다.
	// 이때 점수는 새로 float이 될 수 있기 때문에
	// 새로운 배열에다가 저장해주어야 할 것 같다.
	
	// 그렇게 새롭게 구한 점수들의 합을 가지고 평균을 낸다.

	int n;
	cin >> n;

	int max = 0;
	double total = 0;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		if (a > max) {
			max = a;
		}
		total += a;
	}	

	total = (total / max*100)/ n;
	cout << fixed;
	cout.precision(3);
	cout << total << "\n";
	return 0;
}