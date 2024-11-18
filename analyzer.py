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

#variabelen
listLength = 0
listLength = len(vwList)
totalIncome = 0
averageIncome = 0

totalDrivers = 0

#gemiddeld salaris
if choice =="1":
    for Salaris_bruto in vwList:
        totalIncome += int(Salaris_bruto["Salaris_bruto"])
        averageIncome = totalIncome / listLength

    averageIncome = round(averageIncome)
    print(f"Gemiddeld salaris van alle werknemers:\n{averageIncome} euro")
    
#gemiddeld salaris voor functie X

#aantal werknemers binnen 2 jaar met pensioen

#aantal chauffeurs

elif choice =="4":
    for vw in vwList:
        if vw["Functie"] == "Chauffeur":
            totalDrivers += 1

    print(f"Aantal chauffeurs: {totalDrivers}")

#top 10 langst in dienst
elif choice =="5":
    print(f"Top 10 werknemers langst in dienst:")
    data_sorted = sorted(vwList, key=lambda row:(row["Datum in dienst"]), reverse=True)
    for i in range(10):
        date_hired = data_sorted[i]
        print(f"{date_hired['Voornaam']}, {date_hired['Achternaam']}, {date_hired['Datum in dienst']}")

#aantal medewerkers met functie X bij afdeling Y

#export (w)
#exit (x)