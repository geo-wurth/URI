#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	string nome;
	double salario, vendas, comissao;
	cin >> nome >> salario >> vendas;
	comissao = vendas * 0.15;
	cout << fixed << setprecision(2) << "TOTAL = R$ " << salario + comissao << endl;
	return 0;
}
