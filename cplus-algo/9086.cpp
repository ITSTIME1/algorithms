#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	// 문자열을 받기 위해서 string을 사용해보자
	// 먼저 테스트 케이스가 주어지니까 테스트 케이스를 받아주자.
	int testCase;
	cin >> testCase;
	// 줄어들다가 0이 되면 false가 되기 때문에 while문을 빠져나온다.
	while (testCase--) {
		string s;
		cin >> s;
		cout << s[0] << s[s.size()-1] << "\n";

	} 
	return 0;
}