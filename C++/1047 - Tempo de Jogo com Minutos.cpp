#include <iostream>

using namespace std;

int main(){
	int h_ini, h_ter, min_ini, min_ter, tempo_total, tempo_ini, tempo_ter, tempo_h, tempo_min, aux;
	cin >> h_ini >> min_ini >> h_ter >> min_ter;
	tempo_ini = ((h_ini * 60) + min_ini);
	tempo_ter = ((h_ter * 60) + min_ter);
	if ((h_ini == h_ter) and (min_ini == min_ter) and (h_ini == min_ini)){
		tempo_h = 24;
		tempo_min = 0;
	}
	else if ((h_ter < h_ini) or ((h_ini == h_ter) and (min_ini > min_ter))){
		tempo_total = (24*60) - tempo_ini + tempo_ter;
		tempo_h = tempo_total / 60;
		tempo_min = tempo_total % 60;
	}
	else{
		tempo_total = tempo_ter - tempo_ini;
		tempo_h = tempo_total / 60;
		tempo_min = tempo_total % 60;
	}

	
	cout << "O JOGO DUROU " << tempo_h << " HORA(S) E " << tempo_min << " MINUTO(S)" << endl;
	return 0;
}
