#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 

	string s;
	getline(cin, s);

	int cnt = 0;
	for (int i = 0; i < s.length(); i++) {
		// 공백을 검사할때도 ' ' char형태 그래도 받아주어야함.
		if (s[i] == ' ') {
			cnt += 1;
		}	
	}	
	// 마지막까지 해야 하니까
	cnt += 1;
	// 근데 앞뒤로 공백 들어오는건 빼자
	// 둘다 들어올 수도 있자나
	if(s[0] == ' ') {
		cnt -= 1;
	}
	if(s[s.length()-1] == ' ') {
		cnt -= 1;
	}
	cout << cnt << "\n";
	
	return 0;
}
