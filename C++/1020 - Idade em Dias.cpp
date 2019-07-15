#include <iostream>

using namespace std;

int main(){
	int tempo, dia, mes, ano;
	cin >> tempo;
	ano = tempo / 365;
	mes = tempo % 365;
	dia = mes % 30;
	mes = mes / 30;
	cout << ano << " ano(s)" << endl;
	cout << mes << " mes(es)" << endl;
	cout << dia << " dia(s)" << endl;
	return 0;
}
