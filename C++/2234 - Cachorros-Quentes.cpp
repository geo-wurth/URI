#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
 
    float H, P, media;
    cin >> H >> P;
 	media = H / P;
 	cout << setprecision (2) << fixed << media << endl;
    return 0;
}
