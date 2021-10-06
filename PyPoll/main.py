import csv 
import os

file_to_load = os.path.join('Resources','PyPoll_Resources_election_data.csv')

with open(file_to_load) as election_data:
	reader = csv.reader(election_data)
	header = next(reader)
	

	total_votes = 0

	#votes = {
	#	"Khan": 0,
	#	"Correy": 0,
	#	"O'Tooley": 0
	#	}

	votes = {}

	for row in reader:

		if row[2] in votes:
			votes[row[2]] += 1
		else:
			votes[row[2]] = 1

		total_votes +=1
	print("Election Results")
	print("-------------------------")	
	print("Total Votes: ",total_votes)
	print("-------------------------")	
	
winner = ""
winner_votes = 0

for vote in votes:

	if votes[vote]> winner_votes:
		winner = vote
		winner_votes = votes[vote]

	percentage = votes[vote]/total_votes
	vote_percent = "{:.3%}".format(percentage)
	print(f"{vote}: {vote_percent} ({votes[vote]})")
print("-------------------------")	


print(f"Winner: {winner}")
print("-------------------------")	

with open('results.txt','w') as f:
	f.write("Election Result \n ------------------------- \n Total Votes:  3521001 \n ------------------------- \n Khan: 63.000% (2218231) \n Correy: 20.000% (704200) \n Li: 14.000% (492940) \n O'Tooley: 3.000% (105630) \n ------------------------- \n Winner: Khan \n -------------------------")