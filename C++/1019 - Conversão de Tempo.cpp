#include <iostream>

using namespace std;

int main(){
	int tempo, hora, min, seg;
	cin >> tempo;
	seg = tempo % 60;
	min = tempo / 60;
	hora = min / 60;
	min = min % 60;
	cout << hora << ":" << min << ":" << seg << endl;	
	return 0;
}
