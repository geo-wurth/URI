#include <iostream>
#include <stdlib.h>

using namespace std;

int main(){
	int A, B, C, maior, maior2;
	cin >> A >> B >> C;
	maior = ((A + B + abs( A - B )) / 2);
	maior2 = ((maior + C + abs( maior - C )) / 2);
	cout << maior2 << " eh o maior" << endl;
	return 0;
}
