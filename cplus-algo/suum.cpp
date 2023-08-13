#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n;
	cin >> n;
	// string s;
	// // 혹은 char를 사용해서
	// // 최대 100 만큼들어오니까 100만큼의 배열공간을 만들어준뒤.
	// char a[100];

	// // 해당 입력을 문자형태로 받아서
	// // 배열 한칸한칸 저장한다.

	// // 이후 a를 순회하면서 아래와 같은 방법으로도 가능하다.
	// cin >> s;
	// int total = 0;
	// for (int i = 0; i < n; i++) {
	// 	// 아스키 코드값 0에서 빼주면
	// 	// 현재 문자가 정수로 바뀌어 더해진다.
	// 	total += s[i] - '0';
	// 	total += a[i] - '0';
	// }

	// cout << total << "\n";
	char num2;
	int result = 0;
	for (int i = 0; i < n; i++) {
		// cin은 기본적으로 공백이 들어오면 문자가 끝난걸로 판단하니까
		// 하나씩 입력받아서
		// 그 입력받은 각각을 문자에서 정수로 변환해줄 수 있겠네.
		cin >> num2;
		// cout << num2 << "\n";
		result += (num2 - '0');
		// cout << num2-'0' << "\n";
		// cout << num2 << "\n";
	}
	cout << result << "\n";

	
	// string을 선언해서 받는방법
	// string으로 받았으니 s만큼 순회하면서 문자->정수로 바꾸는 방법
	// char를 선언해서 char로 하나씩 받아오면서 문자->정수로 바꾸는 방법
	// char를 쓰되 공간을 할당하지 않고 바로 선언만 한뒤 입력을 받아 한문자씩 바꾸는 방법.
	return 0;
}