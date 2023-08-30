#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n;
	string word;
	int count = 0;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> word;
		bool alphabet[26] = {false, };

		// 이렇게 풀수 있네 아스키 익숙치가 않네;
		// 'a'의 아스키코드값이 97이니까 해당 단어에서 'a'를 빼서 해당 단어의 인덱스를 얻음.
		// 그러면 이 인덱스는 해당 알파벳이 있을 index가 됨.
		alphabet[(int)(word[0])-97] = true;
		for (int j = 1; j < word.size(); j++) {
			if (word[j] == word[j-1]) {
				continue;
				// 연속적이면서 단어가 나온경우는없자나.
				// 연속적이지 않으면서 단어가 이미 나온 경우라면
			} else if(word[j] != word[j-1] && alphabet[(int)word[j] - 97] == true) {
				count += 1;
				break;
			} else {
				// 연속적이지 않거나 또는 알파벳이 false인 경우
				alphabet[(int)word[j] - 97] = true;
			}
		}
	}

	cout << n - count << "\n";
	return 0; 
}