#include <iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	int n, x;
	cin >> n >> x;
	// 0~ 9999
	// int a[10000];
	// for (int i = 0; i < n; i++) {
	// 	cin >> a[i];
	// }
		
	// for (int i = 0; i < n; i++) {
	// 	if ( x > a[i]) {
	// 		cout << a[i] << " ";
	// 	}
	// }

	// 입력과 동시에 출력 조건이 맞을 경우 출력하게끔
	int val;
	for (int i= 0; i < n; i++ ){
		cin >> val;
		if ( val < x) {
			cout << val << " ";
		}
	} 

	return 0;
}