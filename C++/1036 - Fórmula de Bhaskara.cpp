#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){
	double A, B, C, delta, R1, R2;
	cin >> A >> B >> C;
	delta = (B * B) - (4.0 * A * C);
	if ((delta <= 0) or (A == 0)){
		cout << "Impossivel calcular" << endl;
	}
	else{
		R1 = (((-B) + sqrt(delta)) / (2 * A));
		R2 = (((-B) - sqrt(delta)) / (2 * A));
		cout << fixed << setprecision(5) << "R1 = " << R1 << endl;
		cout << fixed << setprecision(5) << "R2 = " << R2 << endl;
	}
	return 0;
}
