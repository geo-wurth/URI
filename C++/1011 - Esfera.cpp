#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int raio;
	double volume, pi = 3.14159;
	cin >> raio;
	volume = ((4.0/3.0) * pi * raio * raio * raio);
	cout << fixed << setprecision(3) << "VOLUME = " << volume << endl;
	return 0;
}
