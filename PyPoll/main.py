import os
import csv

csvpath = os.path.join('PyPoll', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_votes = 0
    candidates = []
    candidate_votes = {}
    winning_candidate = ""
    winning_votes = 0

    for row in csvreader:
        total_votes += 1
        #to find the total votes

        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        #to find candidates names, votes, and percentage of votes
        #if not in the candidate list, add the name and begin tracking that candidates vote count
        #add vote to candidate count

f = open("Analysis.txt", "a")
print("Election Results", file=f)
print("-------------------------", file=f)
print("Total Votes:", total_votes, file=f)
print("-------------------------", file = f)

for candidate_name, votes in candidate_votes.items():
    percentage_won = (votes / total_votes) * 100
    #find the percentage won
    candidate_results = f"{candidate_name}: {percentage_won:.3f}% ({votes})"
    #print candidate name, percentage of votes, and votes
    print(candidate_results, file=f)

    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate_name
       #true then set winning count to that candidate and their votes/% 

print("-------------------------", file=f)
print("Winner:", winning_candidate, file=f)
