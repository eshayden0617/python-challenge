import os
import csv

csvpath = os.path.join('PyPoll/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_votes = 0
    candidates_dict = {}
    #to store cnaidate name and number of votes

    for row in csvreader:
        total_votes += 1
        #find total votes

        candidate_name = row[2]
        if candidate_name not in candidates_dict:
            candidates_dict[candidate_name] = {'votes': 0, 'percentage': 0}
        candidates_dict[candidate_name]['votes'] +=1
        #look through the third row and find candidate names,
        #if name not in dictionary variable, add it then go to next row along with votes and percentage 
        #if name in dictionary variable, skip it

for candidate in candidates_dict:
    votes = candidates_dict[candidate]['votes']
    percentage = (votes / total_votes) * 100
    candidates_dict[candidate]['percentage'] = percentage
    #finding the number of votes each candidate had and percentage they won by

#f = open("Analysis.txt")
print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
for candidate, data in candidates_dict.items():
    votes = data['votes']
    percentage = data['percentage']
    print(candidate + ": " + str(percentage) + "% (" + str(votes) + ")")
