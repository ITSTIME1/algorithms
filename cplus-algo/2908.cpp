#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	// 일단 숫자를 받아주고
	// stoi함수를 상해서 string to irnteger 로 변경한다음
	// 두 수중 큰 수를 말하게 하면된다.

	string a;
	string b; 
	cin >> a >> b;

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());

	if (stoi(a) > stoi(b)) {
		cout << a << "\n";
	} else {
		cout << b << "\n";
	}
	
	

	
	return 0;
}