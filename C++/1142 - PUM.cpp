#include <iostream>
 
using namespace std;
 
int main() {
 
    int N;
    cin >> N;
    int x = 1;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < 3; ++j) {
		  cout << x << " ";
		  x++;
		}
	cout << "PUM" << endl;
	x++;
	} 
	
    return 0;
}
