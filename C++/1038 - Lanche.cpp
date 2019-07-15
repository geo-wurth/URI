#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int item, qtd;
	double valor;
	cin >> item >> qtd;
	switch (item){
		case 1:
			valor = qtd * 4;
			break;
		case 2:
			valor = qtd * 4.5;
			break;
		case 3:
			valor = qtd * 5;
			break;
		case 4:
			valor = qtd * 2;
			break;
		case 5:
			valor = qtd * 1.5;
			break;
	}
	cout << fixed << setprecision(2) << "Total: R$ " << valor << endl;
	return 0;
}
