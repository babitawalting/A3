#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#import os to clear screen
import os
#import datetime for choice 3 and 5
from datetime import datetime

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

    choice = input("\nKies een nummer of letter uit het menu: ")

    os.system("cls")

#variables
    listLength = len(vwList)

#gemiddeld salaris
    if choice =="1" or choice =="w":
        totalIncome = 0
        averageIncome = 0
        outputA = ""

        for Salaris_bruto in vwList:
            totalIncome += int(Salaris_bruto["Salaris_bruto"])
            averageIncome = totalIncome / listLength
            averageIncome = round(averageIncome)
        
        outputA += (f"1. Gemiddeld salaris van alle werknemers: {averageIncome} euro\n")     
        if choice == "1":
            print(f"{outputA}")
            input("---------------\nDruk op enter om door te gaan")
            os.system("cls")
        else:
            exportTime= datetime.now()
            myReport.write(f'Statistieken berekend op: {exportTime.strftime("%Y-%m-%d, %H:%M:%S")}'+ '\n')
            myReport.write(f'{outputA}')
            myReport.flush() #Flush zodat naar file wordt geschreven

#gemiddeld salaris voor functie X
    if choice =="2" or (choice.lower() == "w"):
        totalFunctionIncome = 0
        averageFunctionIncome = 0
        outputB = ""
        function = input("Voer een functie in waar je het gemiddelde salaris van wilt weten\n")
        os.system("cls")

        for vw in vwList:
            if vw["Functie"] == function and (vw["Salaris_bruto"]):
                totalFunctionIncome += int(vw["Salaris_bruto"])
        averageFunctionIncome = totalFunctionIncome / listLength
        averageFunctionIncome = round(averageFunctionIncome)
        
        outputB += f"2. Gemiddelde salaris van {function}: {averageFunctionIncome} euro"
        if choice == "2":
            print(f"{outputB}")
            input("\n---------------\nDruk op enter om door te gaan")
            os.system("cls")
        else:
            myReport.write(f'{outputB}' + '\n')
            myReport.flush() #Flush zodat naar file wordt geschreven

#aantal werknemers binnen 2 jaar met pensioen
    if choice == "3" or (choice.lower() == "w"):
        totalEmployeesRetirement = 0
        d1 = datetime(1959, 12, 31)
        d2 = datetime(1957, 1, 1)
        outputC = ""

        for vw in vwList:
            geboortedatum = datetime.strptime(vw["Geboortedatum"], "%d-%m-%Y")
            if d2 <= geboortedatum <= d1:
                totalEmployeesRetirement += 1
        
        outputC += f"3. Aantal werknemers binnen 2 jaar met pensioen: {totalEmployeesRetirement}"
        if choice == "3":
            print(f"{outputC}")
            input("\n---------------\nDruk op enter om door te gaan")
            os.system("cls")
        else:
            myReport.write(f'{outputC}' + '\n')
            myReport.flush() #Flush zodat naar file wordt geschreven
    
#aantal chauffeurs
    if choice =="4"  or (choice.lower() == "w"):
        totalDrivers = 0
        outputD = ""

        for vw in vwList:
            if vw["Functie"] == "Chauffeur":
                totalDrivers += 1

        outputD += f"4. Aantal chauffeurs: {totalDrivers}"
        if choice == "4":
            print(f"{outputD}")
            input("\n---------------\nDruk op enter om door te gaan")
            os.system("cls")
        else:
            myReport.write(f'{outputD}' + '\n')
            myReport.flush() #Flush zodat naar file wordt geschreven'

#top 10 langst in dienst
    if choice =="5" or (choice.lower() == "w"):
        outputE= ""
        data_sorted = sorted(vwList, key=lambda row: datetime.strptime(row["Datum in dienst"], "%d-%m-%Y"))
        for i in range(10):
            longestEmployed = data_sorted[i]
            outputE += f"- {longestEmployed['Voornaam']} {longestEmployed['Achternaam']} sinds: {longestEmployed['Datum in dienst']} \n"
        
        if choice == "5":
            print(f"Top 10 werknemers langst in dienst:")
            print(f"{outputE}")
            input("---------------\nDruk op enter om door te gaan")
            os.system("cls")
        else:
            myReport.write(f"5. Top 10 werknemers langst in dienst:\n")
            myReport.write(f'{outputE}')
            myReport.flush() #Flush zodat naar file wordt geschreven

#aantal medewerkers met functie X bij afdeling Y
    if choice =="6" or (choice.lower() == "w"):
        print(f"Aantal medewerkers met functie X bij afdeling Y")
        functionChoice = input("Welke functie?\n")
        departmentChoice = input("Welke afdeling?\n")
        employeeCount = 0
        outputF = ""
    
        for vw in vwList:
            if vw["Functie"] == functionChoice and vw["Afdeling"] == departmentChoice:
                employeeCount += 1


        outputF += f"Aantal medewerkers met functie {functionChoice} bij afdeling {departmentChoice}: {employeeCount}"
        if choice == "6":
            print(f"{outputF}")
            input("\n---------------\nDruk op enter om door te gaan")
            os.system("cls")
        else:
            myReport.write(f'6. {outputF}' + '\n')
            myReport.flush() #Flush zodat naar file wordt geschreven
            os.system("cls")
            print("Data-analyse geëxporteerd!")
            choice = input("\n---------------\nDruk op enter om door te gaan of druk x om te stoppen: ")
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

