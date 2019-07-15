x = float(input())
if (x <= 2000):
    print("Isento")
elif (2000 < x <= 3000):
    x = x - 2000
    imposto = x * 0.08
    print("R$ %.2f"%imposto)
elif (3000 < x <= 4500):
    x = x - 2000
    imposto = 999.99 * 0.08
    x = x - 999.99
    imposto = imposto + (x * 0.18)
    print("R$ %.2f"%imposto)
elif (3000 < x <= 4500):
    x = x - 2000
    imposto = 999.99 * 0.08
    x = x - 999.99
    imposto = imposto + (x * 0.18)
    print("R$ %.2f"%imposto)
else:
    x = x - 2000
    imposto = 1000 * 0.08
    x = x - 1000
    imposto = imposto + (1500 * 0.18)
    x = x - 1500
    imposto = imposto + (x * 0.28)
    print("R$ %.2f"%imposto)
