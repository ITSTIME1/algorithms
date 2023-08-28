#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	char charArray[] = "Hello, World!";
	// 해당 타입이 charArray에 몇개가 들어가냐
	// 즉 해당 타입의 바이트가 저 배열의 몇개가 들어가냐 이 뜻이네
	// 그렇구만
    int size = sizeof(charArray) / sizeof(char); // 배열의 크기 계산


    // 문자형 배열 13의 길이에 null문자까지
    // 해당 방법은 컴파일타임에 계산을 하는 것이기 때문에
    // 동적으로 할당된 배열이나 함수의 파라미터로 전달된 배열에는 사용할 수 없다.
    
    cout << size << "\n";
	return 0;
}