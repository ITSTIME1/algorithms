#include <iostream>
using namespace std;

int main(void) {

	int N;
	int total = 0;
	cin >> N;


	for (int i = 1; i <= N; i++){
		total += i;
	}
	cout << total << endl;
	return 0;
}