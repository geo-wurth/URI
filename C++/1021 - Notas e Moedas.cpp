#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double valor;
	int c100, c50, c20, c10, c5, c2, m100, m50, m25, m10, m5, m1, notas, moedas;
	cin >> fixed >> setprecision(2) >>valor;
	notas = valor;
	moedas = (valor * 100) - (notas * 100);
// contagem das notas
	for (c100 = 0; notas >= 100; c100++){
		notas = notas - 100;
	}
	for (c50 = 0; notas >= 50; c50++){
		notas = notas - 50;
	}
	for (c20 = 0; notas >= 20; c20++){
		notas = notas - 20;
	}
	for (c10 = 0; notas >= 10; c10++){
		notas = notas - 10;
	}
	for (c5 = 0; notas >= 5; c5++){
		notas = notas - 5;
	}
	for (c2 = 0; notas >= 2; c2++){
		notas = notas - 2;
	}
// contagem das moedas
	for (m100 = 0; notas >= 1; m100++){
		notas = notas - 1;
	}
	for (m50 = 0; moedas >= 50; m50++){
		moedas = moedas - 50;
	}
	for (m25 = 0; moedas >= 25; m25++){
		moedas = moedas - 25;
	}
	for (m10 = 0; moedas >= 10; m10++){
		moedas = moedas - 10;
	}
	for (m5 = 0; moedas >= 5; m5++){
		moedas = moedas - 5;
	}
	for (m1 = 0; moedas >= 1; m1++){
		moedas = moedas - 1;
	}
	
	
	cout << "NOTAS:" << endl;
	cout << c100 << " nota(s) de R$ 100.00" << endl;
	cout << c50 << " nota(s) de R$ 50.00" << endl;
	cout << c20 << " nota(s) de R$ 20.00" << endl;
	cout << c10 << " nota(s) de R$ 10.00" << endl;
	cout << c5 << " nota(s) de R$ 5.00" << endl;
	cout << c2 << " nota(s) de R$ 2.00" << endl;
	cout << "MOEDAS:" << endl;
	cout << m100 << " moeda(s) de R$ 1.00" << endl;
	cout << m50 << " moeda(s) de R$ 0.50" << endl;
	cout << m25 << " moeda(s) de R$ 0.25" << endl;
	cout << m10 << " moeda(s) de R$ 0.10" << endl;
	cout << m5 << " moeda(s) de R$ 0.05" << endl;
	cout << m1 << " moeda(s) de R$ 0.01" << endl;
	return 0;
}
