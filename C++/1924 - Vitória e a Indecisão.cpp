#include <iostream>
#include <string> 
 
using namespace std;
 
int main() {
 
	int Cursos = 1, i = 1;
	string textos[2000];
 	cin >> Cursos;
 	while (i <= Cursos){
	 	cin >> textos[i];
	 	i = i + 1;
	 }
 	
 	cout << "Ciencia da Computacao" << endl;
 	
    return 0;
}
