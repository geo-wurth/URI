#include <iostream>
 
using namespace std;
 
int main() {
 
	int N = 1, i = 1, ano, Tempos[2000];
 	cin >> N;
 	while (i <= N){
	 	cin >> ano;
	 	ano -= 2015;
		if (ano < 0){
			 cout << -ano << " D.C." << endl; 
		 }
		else{
		 	 cout << (ano + 1) << " A.C." << endl; 
		 } 
		 ++i;
	 }
 	
    return 0;
}
