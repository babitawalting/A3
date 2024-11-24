#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#import os to clear screen
import os
#import datetime for choice 3 and 5
import datetime

isRunning = True
while isRunning:
#start-menu
    os.system("cls")
    
    print("Data-analyse")
    print("1. Gemiddeld salaris")
    print("2. Gemiddelde salaris van functie X")
    print("3. Aantal werknemers binnen 2 jaar met pensioen")
    print("4. Aantal chauffeurs")
    print("5. Top 10 langst in dienst")
    print("6. Aantal medewerkers met functie X bij afdeling Y")
    print("W. Informatie exporteren naar een apart bestand")
    print("X. Programma sluiten")

    choice = input("\nKies een nummer uit het menu of druk x om te stoppen: ")

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
        input("\n---------------\nDruk op enter om door te gaan")
        os.system("cls")
    
#gemiddeld salaris voor functie X
    if choice =="2":
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

        input("\n---------------\nDruk op enter om door te gaan")
        os.system("cls")

#aantal werknemers binnen 2 jaar met pensioen
    if choice == "3":
        totalEmployeesRetirement = 0
        d1 = datetime.date(1959, 12, 31)
        d2 = datetime.date(1957, 1, 1)

        for vw in vwList:
            geboortedatum = datetime.datetime.strptime(vw["Geboortedatum"], "%d-%m-%Y").date()
            if d2 <= geboortedatum <= d1:
                totalEmployeesRetirement += 1
        
        print(f"Aantal werknemers binnen 2 jaar met pensioen: {totalEmployeesRetirement}")
        
        input("\n---------------\nDruk op enter om door te gaan")
        os.system("cls")
    
#aantal chauffeurs
    if choice =="4":
        totalDrivers = 0
        for vw in vwList:
            if vw["Functie"] == "Chauffeur":
                totalDrivers += 1

        print(f"Aantal chauffeurs: {totalDrivers}")

        input("\n---------------\nDruk op enter om door te gaan")
        os.system("cls")

#top 10 langst in dienst
    if choice =="5":
        print(f"Top 10 werknemers langst in dienst:")
        data_sorted = sorted(vwList, key=lambda row:datetime.datetime.strptime(row["Datum in dienst"], "%d-%m-%Y"), reverse=False)
        for i in range(10):
            longestEmployed = data_sorted[i]
            print(f"{longestEmployed['Voornaam']}, {longestEmployed['Achternaam']}, {longestEmployed['Datum in dienst']}")

        input("\n---------------\nDruk op enter om door te gaan")
        os.system("cls")

#aantal medewerkers met functie X bij afdeling Y
    if choice =="6":
        print(f"Aantal medewerkers met functie X bij afdeling Y")
        functionChoice = input("Welke functie?\n")
        departmentChoice = input("Welke afdeling?\n")
        employeeCount = 0
    
        for vw in vwList:
            if vw["Functie"] == functionChoice and vw["Afdeling"] == departmentChoice:
                employeeCount += 1
        print(f"\nAantal medewerkers met functie {functionChoice} bij afdeling {departmentChoice}: {employeeCount}")

        input("\n---------------\nDruk op enter om door te gaan")
        os.system("cls")


#export (w)
    if (choice.lower() == "w"):

#gemiddeld salaris(w)
        totalIncome = 0
        averageIncome = 0

        for Salaris_bruto in vwList:
            totalIncome += int(Salaris_bruto["Salaris_bruto"])
            averageIncome = totalIncome / listLength

        averageIncome = round(averageIncome)

#gemiddeld salaris voor functie X(w)
        totalFunctionIncome = 0
        averageFunctionIncome = 0
        function = input("Voer een functie in waar je het gemiddelde salaris van wilt weten\n")
        os.system("cls")

        for vw in vwList:
            if vw["Functie"] == function and (vw["Salaris_bruto"]):
                totalFunctionIncome += int(vw["Salaris_bruto"])
        averageFunctionIncome = totalFunctionIncome / listLength
        averageFunctionIncome = round(averageFunctionIncome)
        os.system("cls")

#aantal werknemers binnen 2 jaar met pensioen(w)
        totalEmployeesRetirement = 0
        d1 = datetime.date(1959, 12, 31)
        d2 = datetime.date(1957, 1, 1)

        for vw in vwList:
            geboortedatum = datetime.datetime.strptime(vw["Geboortedatum"], "%d-%m-%Y").date()
            if d2 <= geboortedatum <= d1:
                totalEmployeesRetirement += 1

#aantal chauffeurs(w)
        totalDrivers = 0
        for vw in vwList:
            if vw["Functie"] == "Chauffeur":
                totalDrivers += 1

#top 10 langst in dienst(w)
        data_sorted = sorted(vwList, key=lambda row:datetime.datetime.strptime(row["Datum in dienst"], "%d-%m-%Y"), reverse=False)
        for i in range(10):
            longestEmployed = data_sorted[i]

#aantal medewerkers met functie X bij afdeling Y(w)
        functionChoice = input("Welke functie?\n")
        departmentChoice = input("Welke afdeling?\n")
        employeeCount = 0
    
        for vw in vwList:
            if vw["Functie"] == functionChoice and vw["Afdeling"] == departmentChoice:
                employeeCount += 1
        
        os.system("cls")

        exportConfirm = input(f"Weet je het zeker dat je wilt exporteren?\nJa: exporteer data\nNee: ga terug naar het menu\n\nBevestig met: ")

        if (exportConfirm.lower() == "ja"):
            myReport.write('-------------------------------------' + '\n' )
            myReport.write('Statistieken berekend op' + '\n' )
            myReport.write(f'Gemiddeld salaris van alle werknemers: {averageIncome} euro' + '\n')
            myReport.write(f'Gemiddeld salaris voor functie {function}: {averageFunctionIncome} euro' + '\n')
            myReport.write(f'Aantal werknemers binnen 2 jaar met pensioen: {totalEmployeesRetirement}' + '\n')
            myReport.write(f'Aantal chauffeurs: {totalDrivers}' + '\n')
            myReport.write(f'{longestEmployed['Voornaam']}, {longestEmployed['Achternaam']}, {longestEmployed['Datum in dienst']}' + '\n')
            myReport.write(f'{longestEmployed['Voornaam']}, {longestEmployed['Achternaam']}, {longestEmployed['Datum in dienst']}' + '\n')
            myReport.write(f'Aantal medewerkers met functie {functionChoice} bij afdeling {departmentChoice}: {employeeCount}' + '\n')
            myReport.flush()
    os.system("cls")

#exit (x)
    if (choice.lower() == "x"):
        confirm = input(f"Weet je het zeker dat je wilt stoppen?\nJa: sluit programma af\nNee: ga terug naar het menu\n\nBevestig met: ")
        
        if (confirm.lower() == "ja"):
            isRunning = False
            os.system("cls")
            print("Data-analyse gesloten. Tot ziens!\n")

#Sluit beide bestanden af
vwFile.close()
myReport.close()