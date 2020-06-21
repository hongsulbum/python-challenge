import os
import csv

csv_reader = os.path.join('Rosources', 'election_data.csv')

# Define Variables
Total_Votes = []
Cadidate_List = []
Win_Percent = []
Win_Number = []
Winner = []

# Open and read csv
with open(csv_reader, newline='') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    firstrow = next(election_data,None)


    for row in election_data:
        Total_Votes.append(row[0])


Total_Votes = len(Total_Votes)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes}")

textoutput = open("vote_analysis.txt","w")
print("Election Results", file=textoutput)
print("-------------------------", file=textoutput)
print(f"Total Votes: {Total_Votes}", file=textoutput)
textoutput.close()
