#include <iostream>

// 표준 네임스페이스를 사용한다는 뜻
// cin, cout, endl 등이
// namespace에 있는 std 클래스에 포함되어 있는 함수들.
// 따라서 위 함수들을 사용하려면 표준 네임스페이스를 정의해서
// 비교적 간편한 문법표현으로 사용이 가능.
// 만약 네임스페이스를 글로벌하게 정의하지 않을 경우
// std::cout
// std::cin 등으로 사용을 해야 하는 번거로움이 존재함.
// :: 이거는 범위 지정 연산자라고 한다.
using namespace std;
   


int main(void) {
   double a, b;

   cout << fixed;
   cout.precision(9);
   cin >> a >> b;
   cout << a / b << endl;

   return 0;
}

