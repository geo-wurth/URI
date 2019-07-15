#include <iostream>
 
using namespace std;
 
int main() {
 
    int N, i;
	cin >> N;
 	for (i = 1; i <= N;){
		  cout << i << " " << i*i << " " << i*i*i << endl;
		 ++i;
		 }
	 
    return 0;
}
