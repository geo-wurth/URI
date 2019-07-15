#include <iostream>

using namespace std;

int main(){
	double P1, P2;
	cin >> P1 >> P2;
	if ((P1 == 0.0) and (P2 == 0.0)){
		cout << "Origem" << endl;
	}
	else if (P1 == 0.0){
		cout << "Eixo Y" << endl;
	}
	else if (P2 == 0.0){
		cout << "Eixo X" << endl;
	}
	else if ((P1 > 0) and (P2 > 0)){
		cout << "Q1" << endl;
	}
	else if ((P1 < 0) and (P2 > 0)){
		cout << "Q2" << endl;
	}
	else if ((P1 < 0) and (P2 < 0)){
		cout << "Q3" << endl;
	}
	else{
		cout << "Q4" << endl;
	}
	return 0;
}
