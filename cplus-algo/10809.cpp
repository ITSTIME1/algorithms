#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;


// c++ stl 에서 제공해주는 find() 함수를 쓰게 된다면
// 쉽게 위치를 찾을 수 있다. find() 함수는 문자열에서 찾을 문자가
// 언제 가장 처음으로 나오게 되는지를 알려준다.
// 따라서 가장 처음으로 나오게 되는 인덱스를 반환해주게 된다.
// 그렇기 때문에 만약 없다면 string::npos가 출력되는데 이때 자료형이 unsigned이기 떄문에
// 2의 보수개념으로 인해 표현할 수 있는 최대 크기의 양수가 출력된다.
// 따라서 이를 방지하기 위해 (int)형으로 캐스팅 해주게 된다면 정상적으로 받아올 수 있다.
// 훨씬 간편하네
void find(string alphabet) {
	for (int i = 0; i < 26; i ++) {
		cout << (int) s.find(alpahbet[i]) << " ";
	}
}




int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);


	int holder[26] = {0,};
	string alphabet = "abcdefghijklmnopqrstuvwxyz";
	string s;
	cin >> s;

	// 알파벳은 주어졌으니
	// 해당 알파벳이랑 똑같다면 그 i를 저장해주면 되는거지.
	// size()만큼 돌면서
	
	// alphabet을 가져오고
	for (int j =0; j < alphabet.size(); j++) {
		// 알파벳을 가져와서 s.size()만큼 검사해보며 처음으로 나온 곳을 검사한다.
		char stand = alphabet[j];
		bool flag = true;
		for (int i = 0; i < s.size(); i++ ){
			// 알파벳이 같다면
			// 중복해서 나온건 피해야되는구나
			if(stand == s[i]) {
				if (holder[j] == 0) {
					holder[j] = i;
					flag = false;
					break;
				}
			}	

		}		
		// 모두 돌아봤는데 없다면	
		if (flag == true) {
			holder[j] = -1;
		}
		
	}
		

	for (int i = 0; i < 26; i++) {
		cout << holder[i] << " ";
	}
	
	
	return 0;
}