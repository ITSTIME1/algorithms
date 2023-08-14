#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	
	int t;
	int index = 1;
	cin >> t;

	while (1) {
		if(t <= 0) {
			break;
		}
		int a, b;
		cin >> a >> b;
		cout << "Case #" << index << ": " << a+b << "\n";
		index ++;
		t--;
	}
	
	return 0;
}