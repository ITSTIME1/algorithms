#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int student = 28;
	// 1~30까지를 범위로 잡고
	// 1~30까지만 확인하면되자나
	int arr[31] = {0};


	for (int i=0; i<student; i++){
		int n;
		cin >> n;
		arr[n] = n;
	}

	for (int i = 1; i < 31; i++) {
		if (arr[i] == 0) {
			cout << i << "\n";
		}
	}
	return 0;
}
