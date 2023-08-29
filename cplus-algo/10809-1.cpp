#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	string s;
	cin >> s; 
	string alphabet = "abcdefghijklmnopqrstuvwxyz";

	for (int i =0; i < 26; i++) {
		cout << (int)s.find(alphabet[i]) << " ";
	}

	
	return 0;
}