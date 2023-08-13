#include <iostream>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	// x, y 가 모두 양수 또는 음수이고 0이 아니다.
	int x;
	int y;
	cin >> x;
	cin >> y;

	if (x > 0 && y > 0) {
		cout << 1 << "\n"; 
	}
	else if ( x < 0 && y > 0) {
		cout << 2 << "\n"; 
	} else if (x < 0 && y < 0) {
		cout << 3<< "\n"; 
	} else if ( x > 0 && y < 0) {
		cout << 4<< "\n"; 
	}
	return 0;
}