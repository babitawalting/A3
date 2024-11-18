#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#start-menu
print("Keuzemenu:")
print("1. Gemiddeld salaris")
print("2. Gemiddelde salaris van functie X")
print("3. Aantal werknemers binnen 2 jaar met pensioen")
print("4. Aantal chauffeurs")
print("5. Top 10 langst in dienst")
print("6. Aantal medewerkers met functie X bij afdeling Y")
print("W. Alle info naar bestand")
print("X. Exit")

isRunning = True
choice = input("Kies een nummer uit het menu: ")

#gemiddeld salaris
listLength = 0
listLength = len(vwList)
totalIncome = 0
averageIncome = 0

if choice =="1":
    for Salaris_bruto in vwList:
        totalIncome += int(Salaris_bruto["Salaris_bruto"])
        averageIncome = totalIncome / listLength

    averageIncome = round(averageIncome)
    print(f"Gemiddeld salaris van alle werknemers:\n{averageIncome} euro")
    
#gemiddeld salaris voor functie X

#aantal werknemers binnen 2 jaar met pensioen

#aantal chauffeurs

#top 10 langst in dienst

#aantal medewerkers met functie X bij afdeling Y

#export (w)
#exit (x)