#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

		
	// 단어의 길이를 출력하라
	// 음 char형의 길이를 측정할 수 있는 방법이 있나.?

	// strlen으로 문자열의 길이를 구할 수 있구나
	// char a[101];
	// cin >> a;
	string s;
	cin >> s;
	cout << s.length() << "\n";
	// cout << strlen(a) << "\n";

	return 0;
	
}