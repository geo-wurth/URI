#include <iostream>

using namespace std;

int main(){
	int A, B, C, A1, B1, C1, aux;
	cin >> A >> B >> C;
	A1 = A;
	B1 = B;
	C1 = C;
	for (int i = 0; i < 3; i++){
		if (A > B){
			aux = A;
			A = B;
			B = aux;
		}
		else if (B > C){
			aux = B;
			B = C;
			C = aux;
		}
	}	
	cout << A << endl << B << endl << C << endl << endl;
	cout << A1 << endl << B1 << endl << C1 << endl;
	return 0;
}
