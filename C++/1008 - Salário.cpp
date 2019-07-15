#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int numero, horas;
	double salarioph, salario;
	cin >> numero >> horas >> salarioph;
	salario = horas * salarioph;
	cout << "NUMBER = " << numero << endl;
	cout << fixed << setprecision(2) << "SALARY = U$ " << salario << endl;
	return 0;
}
