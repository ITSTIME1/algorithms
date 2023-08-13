#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int t;
	cin >> t;
	for (int i=0; i < t; i++) {
		int a=0, b=0;
		cin >> a >> b;
		cout << a + b << "\n";
	}

	return 0;
}
