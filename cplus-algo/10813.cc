#include <iostream>

using namespace std;

void swap(int arr[], int first, int second) {
	int tmp = arr[first];
	arr[first] = arr[second];
	arr[second] = tmp;
}

int main () {

	int n, m;
	cin >> n >> m;

	int arr[101];

	// 바구니의 번호로 공을 초기화하고
	for (int i = 0; i <n; i++) {
		arr[i+1] = i+1;
	}


	for (int i = 0; i < m; i++) {
		int first, second;
		cin >> first >> second;
		swap(arr, first, second);
	}

	for (int i = 1; i < n+1 ; i++) {
		cout << arr[i] << " ";
	}


	return 0;
}