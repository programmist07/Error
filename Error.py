from UseIt import useit
from NoldanBolma import NoldanBolma1
from NolgaKopaytirma import NolgaKopaytirma1

a = int(input("Son kiriting: "))
b = int(input("Son kiriting: "))
c = input("Element kiriting: ")

if (a == 0 or b == 0) and c == "*":
    raise NolgaKopaytirma1("Nolni ko'paytirib bo'miydi")
elif (a < 0 or b < 0) and c == "/":
    raise NoldanBolma1("Adashdiz Brat")
elif c not in ["*", "/", "-", "+"]:
    raise useit("Miyani ishlat")
else:
    if c == '-':
        print(a - b)
    elif c == '+':
        print(a + b)
    elif c == '*':
        print(a * b)
    else:
        print(a // b)




































