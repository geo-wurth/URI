#include <iostream>
#include <iomanip>
#include <tgmath.h>

using namespace std;

int main(){
	long double A, B, C, D, dist;
	cin >> A >> B;
	cin >> C >> D;
	dist = sqrt(pow((C - A),2) + pow((D - B),2));
	cout << fixed << setprecision(4) << dist << endl;
	return 0;
}
