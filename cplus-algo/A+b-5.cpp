#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	while (true) {
		// 둘다 0보다는 크니까 1부터 시작할거고
		int a, b;

		cin >> a >> b;
		if (a == 0 && b == 0) {
			break;
		}

		cout << a + b << "\n";

	}


	
	return 0;
}