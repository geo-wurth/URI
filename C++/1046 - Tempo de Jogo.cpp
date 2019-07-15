#include <iostream>

using namespace std;

int main(){
	int inicio, termino, tempo, aux;
	cin >> inicio >> termino;
	if (inicio > termino){
		tempo = 24 - inicio;
		tempo = tempo + termino;
	}
	else if (inicio == termino){
		tempo = 24;
	}
	else{
		tempo = termino - inicio;
	}
	cout << "O JOGO DUROU " << tempo << " HORA(S)" << endl;
	return 0;
}
