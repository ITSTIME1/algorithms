#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
using namespace std;

void check_out() {}

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	// 배열의 크기를 정해주고 괄호안에 값을 명시하지 않았다면
	// 모든 값은 0으로 초기화 된다.
	// 초기화 리스트는 narrowing cast를 할 수 없다고 하는데
	// 초기화 리스트라는 것은 배열의 값을 초기화 해준 상태를 의미한다.
	// 이때 narrowing cast라는 것은 
	// 암시적인 데이터 손실이 일어나는 것을 의미한다.
	// 예를들어 double 형의 값이 int형으로 바뀌게 된다면
	// 더 작은 타입으로 변경되기 때문에 값의 손실이 발생된다.
	// 이를 narrowing cast 라고 하며 c++ 이전에서 이러한 호환성 문제를 초기화 리스트를 사용해서 해결할 수 있는데
	// 초기화 리스트를 사용하게 되면 narrowing cast가 발생했을때 경고를 보여주게 된다. 
	// 즉 암시적인 데이터 손실이 발생하므로 경고를 보내주게 되는 것이다. 따라서 이를 통해 미리 값의 손실이 일어나는 곳을 알아챌 수 있으며
	// 미리 방지하는데 도움이 된다.
	int arr[30] = {};

	int len = sizeof(arr) / sizeof(int);

	for (int i=0; i < len; i++) {
		if(arr[i] == 0) {
			cout << "this is zero" << " ";
			cout << arr[i] << "\n";
		} else {
			cout << "this is not zero";
		}
		
	}
	// 추가적으로 단어의 길이를 재는 방법이 존재하는데 우선 단어의 길이라고 한다면
	// 문자형의 데이터를 배열로 받아볼 수 있고
	// 혹은 string 라이브러리를 사용해서 string s 로 문자열을 그대로 받을 수 있다.
	// 우선 char형태로 받게 될 경우 string.h헤더 파일에 존재하는 strlen()함수를 사용해서 문자열의 길이를 알 수 있는데
	// 이는 c의 헤더파일이다. 그리고 string라이브러리를 사용하면 size() 함수를 사용해서도 문자열의 길이를 받아볼 수 있다.

	// 따라서 아래와 같이 풀어볼 수 있다.
	// char형으로 받게 될때 string.h 파일에 정의 되어 있는 strlen() 함수를 사용할 수 있다.
	char a[101];
	cin >> a;
	cout << strlen(a); << "\n";


	// string을 사용해서 문자열을 받게되며 이때 size() 함수를 통해서 문자열의 사이즈를 알아낼 수 있다.
	string s;
	cin >> s;
	cout << s.size() << "\n";

	
	return 0;
}