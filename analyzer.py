#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#import os to clear screen
import os
#import datetime for choice 5
import datetime

isRunning = True

#start-menu
os.system("cls")
print("Keuzemenu:")
print("1. Gemiddeld salaris")
print("2. Gemiddelde salaris van functie X")
print("3. Aantal werknemers binnen 2 jaar met pensioen")
print("4. Aantal chauffeurs")
print("5. Top 10 langst in dienst")
print("6. Aantal medewerkers met functie X bij afdeling Y")
print("W. Alle info naar bestand")
print("X. Exit")

choice = input("Kies een nummer uit het menu: ")
os.system("cls")

#variables
listLength = 0
listLength = len(vwList)

#gemiddeld salaris
if choice =="1":
    totalIncome = 0
    averageIncome = 0

    for Salaris_bruto in vwList:
        totalIncome += int(Salaris_bruto["Salaris_bruto"])
        averageIncome = totalIncome / listLength

    averageIncome = round(averageIncome)
    print(f"Gemiddeld salaris van alle werknemers:\n{averageIncome} euro")
    
#gemiddeld salaris voor functie X
elif choice =="2":
    totalFunctionIncome = 0
    averageFunctionIncome = 0
    function = input("Voer een functie in waar je het gemiddelde salaris van wilt weten\n")
    os.system("cls")

    for vw in vwList:
        if vw["Functie"] == function and (vw["Salaris_bruto"]):
            totalFunctionIncome += int(vw["Salaris_bruto"])
    averageFunctionIncome = totalFunctionIncome / listLength

    averageFunctionIncome = round(averageFunctionIncome)
    print(f"Gemiddelde salaris van {function}\n{averageFunctionIncome} euro")

#aantal werknemers binnen 2 jaar met pensioen
elif choice =="3":
    now = datetime.datetime.now()
    print(now.strftime("%d/%m/%Y"))
    


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