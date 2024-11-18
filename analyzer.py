#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#start-menu
print("Keuzemenu:")
print("1. Gemiddelde salaris")
print("2. Gemiddelde salaris van functie X")
print("3. Aantal werknemers binnen 2 jaar met pensioen")
print("4. Aantal chauffeurs")
print("5. Top 10 langst in dienst")
print("6. Aantal medewerkers met functie X bij afdeling Y")
print("W. Alle info naar bestand")
print("X. Exit")
isRunning = True
inputNumber = input("Kies een nummer uit het menu: ")


#gemiddeld salaris
totalIncome = 0
averageIncome = 0
listLength = 0
listLength = len(vwList)

for Salaris_bruto in vwList:
    totalIncome += float(Salaris_bruto["Salaris_bruto"])
    averageValue = totalIncome / listLength

#gemiddeld salaris voor functie X
#aantal werknemers binnen 2 jaar met pensioen

#aantal chauffeurs
totalDrivers = 0

for vw in vwList:
   if vw["Functie"] == "Chauffeur":
    totalDrivers += 1

print(f"Aantal chauffeurs: {totalDrivers}")

#top 10 langst in dienst

#aantal medewerkers met functie X bij afdeling Y

#export (w)
#exit (x)