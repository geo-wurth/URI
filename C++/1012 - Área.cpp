#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double A, B, C, pi = 3.14159, tri, circ, trap, quad, ret;
	cin >> A >> B >> C;
	tri = A * C / 2.0;
	circ = pi * C * C;
	if (A < B){
		trap = ((A * C) + ((B - A) * C / 2.0));
	}
	else{
		trap = ((B * C) + ((A - B) * C / 2.0));
	}
	quad = B * B;
	ret = A * B;
	cout << fixed << setprecision(3) << "TRIANGULO: " << tri << endl << "CIRCULO: " << circ << endl << "TRAPEZIO: " << trap << endl << "QUADRADO: " << quad << endl << "RETANGULO: " << ret << endl;
	return 0;
}
