#include <iostream>
#include <math.h> #pow
 
using namespace std;
 
int main() {
 
    int N = 5;
	int i = 1;
	int N2 = 0;
	int x;
	
	cin >> N;
	while (i <= (N / 2)){
	    x = i * 2;
	    N2 = pow(x, 2);
	    cout << x << "^2 = " << N2 << endl;
		i = i + 1;
	}
 
    return 0;
}


