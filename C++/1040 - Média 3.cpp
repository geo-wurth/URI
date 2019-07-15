#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double N1, N2, N3, N4, M1, M2, NEx;
	cin >> N1 >> N2 >> N3 >> N4;
	M1 = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10);
	cout << fixed << setprecision(1) << "Media: " << M1 << endl;
	if (M1 >= 7.0){
		cout << "Aluno aprovado." << endl;
	}
	else if (M1 < 5.0){
		cout << "Aluno reprovado." << endl;
	}
	else{
		cout << "Aluno em exame." << endl;
		cin >> NEx;
		cout << fixed << setprecision(1) << "Nota do exame: " << NEx << endl;
		M2 = ((M1 + NEx) / 2);
		if (M2 >= 5.0){
			cout << "Aluno aprovado." << endl;
		}
		else{
			cout << "Aluno reprovado." << endl;
		}
		cout << fixed << setprecision(1) << "Media final: " << M2 << endl;
	}
	return 0;
}
