#include <iostream>

using namespace std;

int main(){
	int A = 0, B = 0, div_int = 0;
	double div = 0.0, teste = 0.0;
	cin >> A >> B;
	if (((A % B) == 0) or ((B % A) == 0)){
		cout << "Sao Multiplos" << endl;
	}
	else{
		cout << "Nao sao Multiplos" << endl;
	}
	 return 0;
}
