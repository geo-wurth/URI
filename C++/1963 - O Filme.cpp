#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
 
	double N1 = 0.00, N2 = 0.00, N3 = 0.00;
	while (cin >> N1 >> N2) {
		N3 = (N2 - N1) / N1 * 100;
		cout << setprecision (2) << fixed << N3 <<"%" << endl;
	}
	return 0;
}
