#include <iostream>

using namespace std;

int main(){
	double A, B, C, aux;
	cin >> A >> B >> C;
	for (int i = 0; i < 3; i++){
		if (A < B){
			aux = A;
			A = B;
			B = aux;
		}
		else if (B < C){
			aux = B;
			B = C;
			C = aux;
		}
	}
	if (A >= (B + C)){
		cout << "NAO FORMA TRIANGULO" << endl;
	}
	else if ((A * A) == ((B * B) + (C * C))){
		cout << "TRIANGULO RETANGULO" << endl;
	}
	else if ((A * A) > ((B * B) + (C * C))){
		cout << "TRIANGULO OBTUSANGULO" << endl;
	}
	else if ((A * A) < ((B * B) + (C * C))){
		cout << "TRIANGULO ACUTANGULO" << endl;
	}
	if ((A == B) and (B == C)){
		cout << "TRIANGULO EQUILATERO" << endl;
	}
	else if ((A == B) or (B == C) or (A == C)){
		cout << "TRIANGULO ISOSCELES" << endl;
	}
	return 0;
}
