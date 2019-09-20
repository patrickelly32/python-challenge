import os
import csv


csv_path = os.path.join("../Instructions/PyBank/Resources/budget_data.csv")
csv_path


totalMonths = 0
month = []
totalrev = 0
rev = 0
prerev = 0
deltarev = 0
deltarevList = []


with open(csv_path,'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    for row in csv_reader:
        month.append(row[0])
        deltarevList.append(int(row[1]))
        
totalMonths = len(month)
        
inc = deltarevList[0]
dec = deltarevList[0]


for row in range(len(deltarevList)):
    if deltarevList[row] <= dec:
        dec = deltarevList[row]
        decMonth = month[row]
    if deltarevList[row] >= inc:
        inc = deltarevList[row]
        incMonth = month[row]
    totalrev = totalrev + deltarevList[row]
    
avgDelta = round(totalrev/totalMonths, 2)

dest = os.path.join("../Instructions/PyBank/Resources/budget_data.txt")

print("Financial Analysis" + "\n")
print("------------------------" + "\n")
print("Total Months: " + str(totalMonths) + "\n")
print("Total: $" + str(totalrev) + "\n")
print("Average Change: $" + str(avgDelta) + "\n")
print("Greatest Increase in Profits: " + incMonth + " ($" + str(inc) + ")"+ "\n")
print("Greatest Decrease in Profits: " + decMonth + " ($" + str(dec) + ")"+ "\n")

with open(dest, 'w') as writetxt:
    writetxt.writelines("Financial Analysis" + "\n")
    writetxt.writelines("------------------------" + "\n")
    writetxt.writelines("Total Months: " + str(totalMonths) + "\n")
    writetxt.writelines("Total: $" + str(totalrev) + "\n")
    writetxt.writelines("Average Change: $" + str(avgDelta) + "\n")
    writetxt.writelines("Greatest Increase in Profits: " + incMonth + " ($" + str(inc) + ")"+ "\n")
    writetxt.writelines("Greatest Decrease in Profits: " + decMonth + " ($" + str(dec) + ")"+ "\n")
