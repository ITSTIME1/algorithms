#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;


// 메인 함수
int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int arr[11];
	set<int> s;

	int number = 10;

	// 배열에 숫자를 미리 넣어주고
	for (int i = 0; i < number; i++) {
		int c; 
		cin >> c;
		arr[i+1] = c;
	}	

	// 그 숫자를 42로 나눈 나머지를 set에 저장하자
	for (int i=1; i < number+1; i ++) {
		s.insert(arr[i] % 42);
	}

	cout << s.size() << "\n";
	
	return 0;
}
