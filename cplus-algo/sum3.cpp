#include <iostream>

using namespace std;
// c++의 iostream과 c의 stdio 표준입출력이 동기화 되어있기 때문에
// 두가지 버퍼를 모두 사용하기 때문에 딜레이가 발생한다.

// 따라서 이렇게 동기화 되어 있는걸 끊어주는 역할을 하는게 아래 구문이 된다.
// 끊어주기 때문에 c++만의 독자적인 버퍼가 생겨나고 이말인 즉 c++의 버퍼만 사용하고 c의 버퍼는 사용하지 않게 되니
// 모두 사용했을때보다 버퍼의 수가 줄었기 때문에 시간적인 측면에서 유리하다고 볼 수 있다.


int main(void) {
	ios_base::sync_with_stdio(false);
	// endl 은 단순히 개행 작업만 하는게 아니라 버퍼까지 비우기 때문에
	// 시간 측면에서 더 걸리게 된다. 따라서 "\n" 개행문자를 사용하는게 시간적인 측면에서 유리하다.
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cout << i << "\n";
	}


	return 0;
}