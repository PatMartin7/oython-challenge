import os 
import csv
from statistics import mean	

csvpath = os.path.join('Resources', 'budget_data.csv')
months = []
deltas = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    prev_row = next(csvreader)
    num_rows = 1
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)
        num_rows += 1
        delta = int(row[1]) - int(prev_row[1])
        month = row[0]
        print(delta)
        deltas.append(delta)
        months.append(month)
        prev_row = row
print("Total Months: ", num_rows)
print("Total Changes: ",sum(deltas))
print("Avg Changes: ",round(mean(deltas),2))
res = dict(zip(months,deltas))
print("Max Change: ",max(res, key=res.get), " ",max(deltas))
print("Min Change: ",min(res, key=res.get), " ",min(deltas))