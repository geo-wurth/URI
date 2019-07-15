#include <iostream>

using namespace std;

int main(){
	int valor, valorfixo, c100, c50, c20, c10, c5, c2, c1;
	cin >> valor;
	valorfixo = valor;
	for (c100 = 0; valor >= 100; c100++){
		valor = valor - 100;
	}
	for (c50 = 0; valor >= 50; c50++){
		valor = valor - 50;
	}
	for (c20 = 0; valor >= 20; c20++){
		valor = valor - 20;
	}
	for (c10 = 0; valor >= 10; c10++){
		valor = valor - 10;
	}
	for (c5 = 0; valor >= 5; c5++){
		valor = valor - 5;
	}
	for (c2 = 0; valor >= 2; c2++){
		valor = valor - 2;
	}
	for (c1 = 0; valor >= 1; c1++){
		valor = valor - 1;
	}
	cout << valorfixo << endl;
	cout << c100 << " nota(s) de R$ 100,00" << endl;
	cout << c50 << " nota(s) de R$ 50,00" << endl;
	cout << c20 << " nota(s) de R$ 20,00" << endl;
	cout << c10 << " nota(s) de R$ 10,00" << endl;
	cout << c5 << " nota(s) de R$ 5,00" << endl;
	cout << c2 << " nota(s) de R$ 2,00" << endl;
	cout << c1 << " nota(s) de R$ 1,00" << endl;
	return 0;
}
