import os
import csv

csv_reader = os.path.join("..", "Rosources", "election_data.csv")

#Credite empty dictionary to store name and vote results
election_results = {}

total_votes = 0


# Open and read csv
with open(csv_reader) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    firstrow = next(election_data,None)


    for row in election_data:
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name not in election_results:
            election_results[candidate_name] = 1
        
        else:
            election_results[candidate_name] += 1

#Calculate Winener
winner = max(election_results, key=election_results.get)

print("Election Results")
print("-------------------------")
print(f'Total Votes: {str(total_votes)}')
print("-------------------------")
print(f'Khan: {election_results["Khan"] / total_votes: .3%} ({election_results["Khan"]})')
print(f'Correy: {election_results["Correy"] / total_votes: .3%} ({election_results["Correy"]})')
print(f'Li: {election_results["Li"] / total_votes: .3%} ({election_results["Li"]})')
#print(f"'O'Tooley: {election_results['O'Tooley']/ total_votes: .3%} ({electrion_results['O'Tooley']}")
print("-------------------------")
print(f"Winner: {str(winner)}")
print("-------------------------")

textoutput = open("vote_analysis.txt", "w")
print("Election Results", file=textoutput)
print("-------------------------", file=textoutput)
print(f'Total Votes: {str(total_votes)}', file=textoutput)
print("-------------------------", file=textoutput)
print(f'Khan: {election_results["Khan"] / total_votes: .3%} ({election_results["Khan"]})', file=textoutput)
print(f'Correy: {election_results["Correy"] / total_votes: .3%} ({election_results["Correy"]})', file=textoutput)
print(f'Li: {election_results["Li"] / total_votes: .3%} ({election_results["Li"]})', file=textoutput)
#print(f"'O'Tooley: {election_results['O'Tooley']/ total_votes: .3%} ({electrion_results['O'Tooley']}")
print("-------------------------", file=textoutput)
print(f"Winner: {str(winner)}", file= textoutput)
print("-------------------------", file= textoutput)
textoutput.close()