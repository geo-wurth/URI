#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double A, B, C, per, area;
	cin >> A >> B >> C;
	if( (A < (B + C)) and (B < (A + C)) and (C < (A + B))){
		per = A + B + C;
	    cout << fixed << setprecision(1) << "Perimetro = " << per << endl;
	}
    else{
        area = (((A + B) * C) / 2);
        cout << fixed << setprecision(1) << "Area = " << area << endl;
    }
	return 0;
}
