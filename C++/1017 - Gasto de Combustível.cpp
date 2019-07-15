#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int A, B;
	double dist, comb;
	cin >> A >> B;
	dist = A * B;
	comb = dist / 12.0;
	cout << fixed << setprecision(3) << comb << endl;
	return 0;
}
