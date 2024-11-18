#import csv file
import csv
vwFile = open("VW.csv", "r", encoding="UTF-8")
myReport = open("report.txt", "w")
reader = csv.DictReader(vwFile, delimiter=";")
vwList = list(reader)

#start-menu
print("Kies een optie:")
print("1. Gemiddelde salaris")
print("2. Gemiddelde salaris van functie X")
print("3. Aantal werknemers binnen 2 jaar met pensioen")
print("4. Aantal chauffeurs")
print("5. Top 10 langst in dienst")
print("6. Aantal medewerkers met functie X bij afdeling Y")
print("W. Alle info naar bestand")
print("X. Exit")

