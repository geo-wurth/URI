#include <iostream>
 
using namespace std;
 
int main() {
 
	int T, N[1000], i=0, j=0;
	cin >> T;
	for (i=0;i < 1000;){
	 	for (j=0;j < T;){
	 	 	N[i] = j;
		 	cout << "N[" << i << "] = " << j << endl;
	 	 	++j;
	 	 	if (i<999){
		  	 	 ++i;
			 }else{
		  		return 0;
		  	 }
		  }
	 }
 	
    return 0;
}
