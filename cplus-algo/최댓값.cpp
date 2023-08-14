#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int val=0;
	int index = 0;

	for (int i = 0; i < 9; i++) {
		int n;
		cin >> n;
		if( n > val) {
			val = n;
			index = i+1;
		}
	}
	
	cout << val << "\n";
	cout << index << "\n";
	return 0;
}