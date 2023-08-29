#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	
	// n개의 숫자가 주어진다는 것은
	// 공백없이 숫자의 개수가 n개라는 뜻이기 때문에
	// 총 100개까지를 담을 수 있어야 한다.
	// string으로 받은다음에
	// 해당 숫자들을 문자로 변환해서 더해주면 되지 않을까?
	int n;
	cin >> n;
	string s;
	cin >> s;

	int total = 0;
	for (int i = 0; i < n; i++) {
		// 문자열로 되어 있고 문자열에서 문자하나씩 접근할때는 char형태기 때문에
		// 해당 char형태를 아스키코드로 변환해서 사용 한다면
		// 이때 '0'은 아스키코드상 값이 48 따라서 해당 값을 빼주게 되면
		// 0~9까지의 값을 얻을 수 있는 것이다.
		int num = s[i] - '0';
		total += num;
	}

	cout << total << "\n";
	
	return 0;
}