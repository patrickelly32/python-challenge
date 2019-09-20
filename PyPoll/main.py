import os
import csv 


cand = []
voteList = []
votes = 0
elect = []


electCSV = os.path.join("../Instructions/PyPoll/Resources/election_data.csv")


with open(electCSV) as file:
    electREAD = csv.reader(file)
    
    electROW = next(electREAD)
    
    for electROW in electREAD:
        votes += 1
        candidate = electROW[2]
        if candidate in cand:
            cIndex = cand.index(candidate)
            voteList[cIndex] += 1
        else:
            cand.append(candidate)
            voteList.append(1)
            
perc = []
maxV = voteList[0]
maxInd = 0


for each in range(len(cand)):
    percVote = voteList[each]/votes*100
    perc.append(percVote)
    if voteList[each] > maxV:
        maxV = voteList[each]
        maxInd = each
win = cand[maxInd]

perc = [round(i,2) for i in perc]

print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
for each in range(len(cand)):
    print(f"{cand[each]}: {perc[each]}% ({voteList[each]})")
print("--------------------------")
print(f"Winner: {win}")
print("--------------------------")


output_path = os.path.join("electionResults.txt")
with open(output_path, 'w', newline='') as writeFile:
    csvwriter = csv.writer(writeFile, delimiter=' ')
    csvwriter.writerow("Election Results")
    csvwriter.writerow("--------------------------")
    csvwriter.writerow(f"Total Votes: {votes}")
    csvwriter.writerow("--------------------------")
    for each in range(len(cand)):
        csvwriter.writerow(f"{cand[each]}: {perc[each]}% ({voteList[each]})")
    csvwriter.writerow("--------------------------")
    csvwriter.writerow(f"Winner: {win}")
    csvwriter.writerow("--------------------------")
