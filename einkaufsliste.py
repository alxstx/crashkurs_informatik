einkaufsliste = [
    "Hüttenkäse",
    "Magerquark",
    "Milch",
    "Pistazien",
    "Kohlrabi",
    "Pilze",
    "Couscous"
]

isThere = False

for element in einkaufsliste:
    if element == "Milch":
        isThere = True

if isThere == True:
    print("Milch ist auf der Einkaufsliste")
else:
    print("Milch ist nicht auf der Einkaufsliste")