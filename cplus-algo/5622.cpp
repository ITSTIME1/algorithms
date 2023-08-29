#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	string s[9] = {"", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};

	string word;
	cin >> word;

	int total = 0;
	// 결국 시간복잡도는 word의 길이만큼 돌면 되기 때문에
	// O(N) 선형시간안에 풀린다.
	for (int i=0; i < word.length(); i++) {
		char stand = word[i];
		for (int j = 0 ; j < 9; j++) {
			if((int)s[j].find(stand) != -1) {
				total += j+2;
			}
		}
	}

	cout << total << "\n";
	// n:n+1

	return 0;
}