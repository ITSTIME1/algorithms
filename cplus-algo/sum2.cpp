#include <iostream>
using namespace std;


int main(void) {

	int n;
	int a, b;
	cin >> n;
	while (n > 0) {
		cin >> a >> b;
		cout << a + b << "\n";
		n--;
	}

	return 0;
}