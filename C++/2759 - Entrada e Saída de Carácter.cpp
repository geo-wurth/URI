#include <iostream>
#include <string>
 
using namespace std;
 
int main() {
 
    string A, B, C;
    cin >> A >> B >> C;
    cout << "A = " << A <<", B = " << B << ", C = " << C << "\n" << "A = " << B <<", B = " << C << ", C = " << A << "\n" << "A = " << C <<", B = " << A << ", C = " << B << endl;
	 
    return 0;
}
