#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n, m;
	cin >> n >> m;

	int arr[101];
	// 공의 번호로 일단 넣어주자.
	for (int i = 0; i < n; i++) {
		arr[i+1] = i+1;
	}

	for (int i = 0; i < m; i++) {
		int start, end;
		cin >> start >> end;
		int count = end-start+1;
		// j를 돌릴건데 절반만 돌릴건데
		// 전체사이즈에서 빼줄거다
		// 이렇게 하면 해당 범위에서만 바꿀 수 있다.
		for (int j = start; j < start+(count / 2); j++) {
			int tmp = arr[j];
			arr[j] = arr[end-j+start];
			arr[end-j+start] = tmp;
		}
	}

	for (int i = 1; i < n+1; i++ ) {
		cout << arr[i] << " ";
	}	
	
	return 0;
}
