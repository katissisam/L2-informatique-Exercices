nb_etudiants = int(input("Combien d'étudiants ? "))

notes = []

for i in range(nb_etudiants):
    note = float(input(f"Saisir la note de l'étudiant {i + 1} : "))
    notes.append(note)

admis = 0
for n in notes:
    if n >= 10:
        admis += 1

somme = sum(notes)
moyenne_groupe = somme / nb_etudiants

notes_sup_moyenne = []
for n in notes:
    if n > moyenne_groupe:
        notes_sup_moyenne.append(n)

print("\n--- Résultats ---")
print(f"Notes : {notes}")
print(f"Nombre d'étudiants ayant une note >= 10 : {admis}")
print(f"Moyenne du groupe : {moyenne_groupe:.2f}") 
print(f"Notes supérieures à la moyenne : {notes_sup_moyenne}")