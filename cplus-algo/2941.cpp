#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	string s;
	cin >> s;

	string check;

	// 문자열을 검사할때까지만 하자
	int index = 0;
	string arr[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
	while(index < s.length()) {
		// 우선 index위치부터 문자를 검사해야 되늰데
		// 그냥 다 바꾸고 string길이 계산하면 되겠다.
		for (int i = index; i < index + 3; i++) {
			check += s[i];

			// 1개가 맞는 경우는 없으니까
			if (check.size() == 1) 
				continue;

			bool flag = false;
			for (int j=0; j < 8; j++) {
				if (check == arr[j]) {
					s.replace(index, check.size(), "*");
					flag = true;
					break;
				}
			}
			if(flag) {
				break;
			}

 		}
 		index += 1;
 		check = "";

	}

	cout << index << "\n";
	
	return 0;
}