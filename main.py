


#1
print("""+-------------------------------------+
| ///    Calculateur Frais OM   ///   |
| Software by: Romario                |                                 
| Version: 1.2                        |
| Last update: 10/03/21 14:29         |
+-------------------------------------+
""")
amount = int(input("Entrez le montant: "))

while amount > 1 and amount <= 495:
    print("Frais de retrait: 20F")
    break
while amount > 500 and amount <= 1100:
    print("Frais de retrait: 70F")
    break
while amount > 1105 and amount <= 3000:
    print("Frais de retrait: 135F")
    break
while amount > 3005 and amount <= 5000:
    print("Frais de retrait: 260F")
    break
while amount > 5005 and amount <= 10000:
    print("Frais de retrait: 375F")
    break
while amount > 10005 and amount <= 15000:
    print("Frais de retrait: 525F")
    break
while amount > 15005 and amount <= 20000:
    print("Frais de retrait: 675F")
    break
while amount > 20005 and amount <= 35000:
    print("Frais de retrait: 1050F")
    break
while amount > 35005 and amount <= 60000:
    print("Frais de retrait: 1275F")
    break
while amount > 60005 and amount <= 100000:
    print("Frais de retrait: 1500F")
    break
while amount > 100005 and amount <= 20000000:
    cal = (amount * 1) / 100
    print("Frais de retrait: " + str(cal) + "F")
    amount = int(input("\n\nEntrez le montant: "))


