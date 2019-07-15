from decimal import Decimal

numero = input()

if float(numero) > 0:
    print('+%.4E' % Decimal(numero))
elif float(numero) < 0:
    print('%.4E' % Decimal(numero))
elif float(numero) == 0:
    if numero[0] != "-":
        print('+%.4E' % Decimal(numero))
    else:
        print('%.4E' % Decimal(numero))
