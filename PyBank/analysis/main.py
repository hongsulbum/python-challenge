import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

# Define Variables
Total_Months = []
Profitloss_Total = []
Profit_loss = []
Profitloss_Total = 0
average_change = 0
year_change = []
change = 0


# Open and read csv
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    firstrow = next(csvreader,None)

  #The total number of months included in the dataset
  #The net total amount of "Profit/Losses" over the entire period

    for row in csvreader:
        Total_Months.append(row[0]) 
        Profit_loss.append(int(row[1]))
        Profitloss_Total += int(row[1])

    for i in range(1,len(Profit_loss)):
      change = (Profit_loss[i]) - (Profit_loss[i-1])
      year_change.append(change)
      Total_Change = (sum(year_change))

TotalMonths = len(Total_Months)
Average_Change = (Total_Change/TotalMonths)   
Greatest_Increase = max(year_change)
Greatest_Decrease = min(year_change)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${str(Profitloss_Total)}")
print(f"Average Change: ${str(Average_Change)}")
print(f"Greatest Increase in Profits: ${str(Greatest_Increase)}")
print(f"Greatest Decrease in Profits: ${str(Greatest_Decrease)}")

textoutput = open("analysis.txt", "w")
print("Financial Analysis", file=textoutput)
print("----------------------------", file=textoutput)
print(f"Total Months: {TotalMonths}", file=textoutput)
print(f"Total: ${str(Profitloss_Total)}", file=textoutput)
print(f"Average Change: ${str(Average_Change)}", file=textoutput)
print(f"Greatest Increase in Profits: ${str(Greatest_Increase)}", file=textoutput)
print(f"Greatest Decrease in Profits: ${str(Greatest_Decrease)}", file=textoutput)
textoutput.close()
