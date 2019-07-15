#include <iostream>
#include <string>
 
using namespace std;
 
int main() {
 
	int ocorrencias = 0; 
    string S, New_S, bit1 = "1";
	cin >> S;
  
    for (int i = 0; i < S.length();) {
		if (S[i] == bit1[0]) {
            ++ocorrencias; 
    	}
    ++i;
	}
	ocorrencias = ocorrencias % 2;
	if (ocorrencias == 0) {
		New_S = S + "0";
	}
	else{
		New_S = S + "1";
	}
	
	cout << New_S << endl;
 
    return 0;
}
