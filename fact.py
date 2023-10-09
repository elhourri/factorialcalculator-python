n = int(input("Donnez un nombre : "))
while n <= 0:
    print("Donnez un nombre positif.")
    n = int(input("Donnez un nombre : "))
f = 1
for i in range(1, n , 1):
    f=f*i
print("La factorielle est :", f)