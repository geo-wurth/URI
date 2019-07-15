#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double salario, novo_salario, reajuste_salario;
	int reajuste;
	cin >> salario;
	if ((salario > 0) and (salario <= 400.0)){
		reajuste = 15;
	}
	else if ((salario > 400.0) and (salario <= 800.0)){
		reajuste = 12;	
	}
	else if ((salario > 800.0) and (salario <= 1200.0)){
		reajuste = 10;
	}
	else if ((salario > 1200.0) and (salario <= 2000.0)){
		reajuste = 7;
	}
	else if (salario > 2000.0){
		reajuste = 4;
	}
	reajuste_salario = (salario * reajuste / 100);
	novo_salario = reajuste_salario + salario;
	cout << fixed << setprecision(2) << "Novo salario: " << novo_salario << endl;
	cout << fixed << setprecision(2) << "Reajuste ganho: " << reajuste_salario << endl;
	cout << fixed << setprecision(2) << "Em percentual: " << reajuste << " %" << endl;
	return 0;
}
