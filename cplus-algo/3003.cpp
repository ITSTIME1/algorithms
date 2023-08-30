#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	// 킹, 퀸, 룩, 비숍, 나이트, 폰
	int arr[6] = {1, 1, 2, 2, 2, 8};

	int number[6] = {0, };


	// 동혁이가 찾은 말의 개수를 받아준다.
	for (int i=0; i < 6; i++) {
		cin >> number[i];
	}


	for (int i =0 ; i < 6; i++) {
		number[i] = arr[i] - number[i];
		cout << number[i] << " ";
	}

	
	return 0;
}