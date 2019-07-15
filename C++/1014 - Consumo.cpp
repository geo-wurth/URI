#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int A;
	double B, media;
	cin >> A >> B;
	media = A / B;
	cout << fixed << setprecision(3) << media << " km/l" << endl;
	return 0;
}
