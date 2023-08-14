#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);


	int n;
	int cnt = 1;
	int check = 0; 
	cin >> n;
	check = n;

	while (1) {
		int a, b;
		// 26 2= 20 + 6 = 26
		n = ((n % 10) * 10) + (((n/10) + (n%10)) % 10);
		if (check == n) {
			break;
		}	

		cnt ++;
	}
	cout << cnt << "\n";

	return 0;
}