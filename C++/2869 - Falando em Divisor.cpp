// para testar os sistema deixe como "int main()" o sistema que quer utilizar e "int main2()" e "int main3()" os que ficarão desativados
/*
#include <iostream> // estoura o tempo limite - brute force
 
using namespace std;
 
int main() {
	int casos, numeros, divisor, menor_divisor;
	cin >> casos;
	int resposta[casos];
	for (int i = 1; i <= casos; i++){
		cin >> numeros;
		for (int j = 1; (divisor < numeros) or (divisor != numeros); j++){
			divisor = 0;
			for (int k = 1; k <= j; k++){
				if (j % k == 0){
					divisor++;
				}
			menor_divisor = j;
			}
		}
    	resposta[i] = menor_divisor;
	}
	for (int i = 1; i <= casos; i++){
		cout << resposta[i] << endl;
    }
	return 0;
}

//------------------------------------------------------------------------------------------------

#include <iostream> // resposta aprovada no URI
 
using namespace std;
 
int main() {
	int respostas[101] = {0, 1, 2, 4, 6, 16, 12, 64, 24, 36, 48, 1024, 60, 4096, 192, 144, 120, 65536, 180, 262144, 240, 576, 3072, 4194304, 360, 1296, 12288, 900, 960, 268435456, 720, 73741817, 840, 9216, 196608, 5184, 1260, 719476260, 786432, 36864, 1680, 511620083, 2880, 46480318, 15360, 3600, 12582912, 743685088, 2520, 46656, 6480, 589824, 61440, 595845303, 6300, 82944, 6720, 2359296, 805306368, 134099126, 5040, 536396504, 221225451, 14400, 7560, 331776, 46080, 329376018, 983040, 37748736, 25920, 270016253, 10080, 80065005, 158428766, 32400, 3932160, 746496, 184320, 124160285, 15120, 44100, 534860242, 986564553, 20160, 5308416, 139440954, 415919090, 107520, 140130951, 25200, 2985984, 62914560, 663676353, 231055250, 21233664, 27720, 873523211, 233280, 230400, 45360};
	int casos, numeros;
	cin >> casos;
	int resposta_solicitada[casos];
	for (int i = 1; i <= casos; i++){
		cin >> numeros;
		resposta_solicitada[i] = respostas[numeros];
	}
	for (int i = 1; i <= casos; i++){
		cout << resposta_solicitada[i] << endl;
    }
	return 0;
}

//------------------------------------------------------------------------------------------------
*/
#include <iostream> // falta otimizar a verificação de todas as possibilidades da fatoração do número de divisores para a encontrar o menor número com o determindo divisor
#include <algorithm>

using namespace std;

int main() {
	int primos[27] = {0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
	int fatoracao[10] = {}, j = 0, k = 0, casos, numeros, aux;
	int const M = 1000000007;
	unsigned long long int calculo, aux1, aux2;
	cin >> casos;
	int resposta[casos];
	for (int i = 1; i <= casos; i++){
		cin >> numeros;
		for (j = 2, k = 0; numeros >= primos[j];){
			aux = numeros % primos[j];
			if ( aux == 0){
				numeros = numeros / primos[j];
				fatoracao[k] = primos[j];
				k++;
			}
			else{
				j++;
			}
		}
		sort(fatoracao, fatoracao+k, greater<int>());
		calculo = 1;
		for(int l = 0; l < k; l++){
			aux1 = primos[l + 2];
			aux2 = (fatoracao[l] - 1);
				for (int m = 1; m <= aux2; m++){
					calculo = (calculo * aux1) % M;
				}
		}
		resposta[i] = calculo;
	}
	for (int i = 1; i <= casos; i++){
		cout << resposta[i] << endl;
    }
	return 0;
}
