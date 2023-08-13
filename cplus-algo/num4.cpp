#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int n;
	cin >> n;

	// int a[1000000];
	vector <int> a;
	for (int i= 0; i < n; i++) {
		int b;
		cin >> b;
		a.push_back(b);	
	}
	// stl sort()함수를 사용하게 되면
	// 최악의 경우에도 nlogn을 보장한다.
	// sort(a, a + n);

	// 배열은 첫 인덱스를 가르키기 때무넹
	// sort()는 begin <= arr < end;
	// 범위다 따라서 begin은 배열의 시작을 의미하며
	// end 는 배열의 끝을 의미하기 떄문에
	// 마지막 인덱스인 만약 a 가100이라면 99를 넣는게 아니라
	// 배열의 크기 까지 넣어주어야 제대로 정렬이 가능하다.
	// 범위가 저러니까 만약 크기를 넣어주지 않았다면?

	// begin << arr < 99가 되버린다.
	// 그러면 98까지만 탐새을 진행하기 때문에
	// 제대로된 정렬이 수행이 되지 않는 것이다
	sort(a.begin(), a.end());

	cout << a[0] << " " << a[n-1];



	return 0;
}