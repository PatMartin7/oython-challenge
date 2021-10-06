import os 
import csv
from statistics import mean	

csvpath = os.path.join('Resources', 'budget_data.csv')
months = []
deltas = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    prev_row = next(csvreader)
    num_rows = 1
    
    for row in csvreader:
        num_rows += 1
        delta = int(row[1]) - int(prev_row[1])
        month = row[0]
        deltas.append(delta)
        months.append(month)
        prev_row = row
def results():
    print("Total Months: ", num_rows)
    print("Total Changes: ",sum(deltas))
    print("Avg Changes: ",round(mean(deltas),2))
    res = dict(zip(months,deltas))
    print("Max Change: ",max(res, key=res.get), " ",max(deltas))
    print("Min Change: ",min(res, key=res.get), " ",min(deltas))


output = str(results())


with open('results.txt','w') as f:
    f.write(output)

#having an issue printing the output of the function as a string and writing it to an Excel file, not sure if the homework is asking for us to just hardkey the results to print to text file. 


