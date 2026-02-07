eleves= []

for i in range(3):
    nom= input("Nom de l'éleve ")
    moyenne = float(input("Moyenne : "))

    eleves.append((nom,moyenne))

print("\n Tout les élèves : ")
for élève in eleves:
    print(élève)

print("\n Eleves admis :")
for élève in eleves:
    if élève[1] >=10:
        print(élève)

print("\nEleves ajournés : ")
for élève in eleves:
    if élève <= 10:
        print(élève)

