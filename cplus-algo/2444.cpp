#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// 9..7..5..3..1
// 9+(n-1)*2
// 2n-2+9
// index = 4, start = 9, n = 5, 2*n-1 = 9
// index = 5, start = 7, n = 5, 2*n-2 = 7
// index = 6, start = 5, n = 5, 2*n-3 = 5

// 2*5-1 = 9 - 4 = 5 + 4
// 9 - 5 = 4 + 3
// 9 - 6 = 3 + 2
// 9 - 7 = 2 + 1
// 9 - 8 = 1 + 0
int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n;
	cin >> n;
	int INF = 2*n-1;

	for (int i = 0; i < 2*n-1; i++){
		if (i < INF / 2) {
			for (int j = 0; j < n-i-1; j++) {
				cout << ' ';
			}
			for (int j = 0; j < INF+1; j++) {
				cout << "*";
			}
			cout << "\n";

		} else {
			// 공백을 출력해주고
			for (int j = 0; j < (i+1)-n; j++) {
				cout << ' ';
			}
			for (int j = 0; j < INF-i+(INF-i-1); j++) {
				cout << "*";
			}
			cout << "\n";
		}
	}
	
	return 0;
}