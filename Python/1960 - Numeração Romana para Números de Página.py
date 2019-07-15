numeros = {1: 'I',
           4: 'IV',
           5: 'V',
           9: 'IX',
           10: 'X',
           40: 'XL',
           50: 'L',
           90: 'XC',
           100: 'C',
           400: 'CD',
           500: 'D',
           900: 'CM',
           1000: 'M'}

arabico = int(input())
romano = ""

while arabico != 0:
    if arabico / 900 >= 1:
        romano += numeros[900]
        arabico -=  900
    elif arabico / 500 >= 1:
        romano += numeros[500]
        arabico -= 500
    elif arabico / 400 >= 1:
        romano += numeros[400]
        arabico -= 400
    elif arabico / 100 >= 1:
        romano += numeros[100]
        arabico -= 100
    elif arabico / 90 >= 1:
        romano += numeros[90]
        arabico -= 90
    elif arabico / 50 >= 1:
        romano += numeros[50]
        arabico -= 50
    elif arabico / 40 >= 1:
        romano += numeros[40]
        arabico -= 40
    elif arabico / 10 >= 1:
        romano += numeros[10]
        arabico -= 10
    elif arabico / 9 >= 1:
        romano += numeros[9]
        arabico -= 9
    elif arabico / 5 >= 1:
        romano += numeros[5]
        arabico -= 5
    elif arabico / 4 >= 1:
        romano += numeros[4]
        arabico -= 4
    elif arabico / 1 >= 1:
        romano += numeros[1]
        arabico -= 1

print(romano)
