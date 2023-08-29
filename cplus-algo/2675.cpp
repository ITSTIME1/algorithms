#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int t;
	cin >> t;
		
	while(t--) {
		int r;
		string s;
		cin >> r >> s;

		for (int i= 0; i < s.size(); i++) {
			char stand = s[i];
			for (int j = 0; j < r; j++ ){
				cout << stand << "";
			}
		}
		cout << "\n";
	}

	return 0;
	
}

// 그럼 문자열의 길이가 8이라면
// r번이 3번이라면
// 첫번째 문자에서 * 3
// 두번째 문자에서 * 3
// 따라서 문자열의 길이 * 3
// 24번 하게 되는거지