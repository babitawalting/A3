#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#import datetime for choice 5
import datetime

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
totalFunctionIncome = 0
averageFunctionIncome = 0

if choice =="1":
    for Salaris_bruto in vwList:
        totalIncome += int(Salaris_bruto["Salaris_bruto"])
        averageIncome = totalIncome / listLength

    averageIncome = round(averageIncome)
    print(f"Gemiddeld salaris van alle werknemers:\n{averageIncome} euro")
    
#gemiddeld salaris voor functie X
elif choice =="2":
    function = input("Voer een functie in waar je het gemiddeld van wilt weten: ")
    for Salaris_Bruto in vwList:
        averageFunctionIncome = totalFunctionIncome / listLength
    print(f"Gemiddelde salaris van {function}:\n{averageFunctionIncome} euro")


#aantal werknemers binnen 2 jaar met pensioen

#aantal chauffeurs
elif choice =="4":
    totalDrivers = 0
    for vw in vwList:
        if vw["Functie"] == "Chauffeur":
            totalDrivers += 1

    print(f"Aantal chauffeurs: {totalDrivers}")

#top 10 langst in dienst
elif choice =="5":
    print(f"Top 10 werknemers langst in dienst:")
    data_sorted = sorted(vwList, key=lambda row:datetime.datetime.strptime(row["Datum in dienst"], "%d-%m-%Y"), reverse=False)
    for i in range(10):
        longestEmployed = data_sorted[i]
        print(f"{longestEmployed['Voornaam']}, {longestEmployed['Achternaam']}, {longestEmployed['Datum in dienst']}")

#aantal medewerkers met functie X bij afdeling Y
elif choice =="6":
    print(f"Aantal medewerkers met functie X bij afdeling Y:")
    functionChoice = input("Welke functie?")
    departmentChoice = input("Welke afdeling?")
    employeeCount = 0
    
    for vw in vwList:
        if vw["Functie"] == functionChoice and vw["Afdeling"] == departmentChoice:
            employeeCount += 1
    print(f"Aantal medewerkers met functie {functionChoice} bij afdeling {departmentChoice}: {employeeCount}")

#export (w)


#exit (x)