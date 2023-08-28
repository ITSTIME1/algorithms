#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	// 끝에 null문자까지 들어오니까
	char a[10001];
	cin >> a;
	int r;
	cin >> r;

	cout << a[r-1] << "\n";

	return 0;
}
