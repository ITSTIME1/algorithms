// 전 처리기 지시어라고 한다.

// 이게 입출력 라이브러리네 c++ 표준 라이브러리
// std::cout 를 쓰기 전에 반드시 신언을 해야 된다는거고

#include <iostream>
using namespace std;

int main() {
    // cout == Character output
    // std::cout << "Hello World!";
    // 주소를 접근하기 위해서 object로 접근한다는데
    // 
    std::cout << "Hello World!\nName!";
    return 0;
}

