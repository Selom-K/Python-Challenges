# Set Dependencies:
import os
import csv

# Declare Variables:
candidate_list = []
voting_list = []
percent_list = []
number_of_votes = 0
candidate = 0
winner = 0

# Describe the file path to the csv file:
csv_path = os.path.join('Resources', 'election_data.csv')

# Opening and reading the file:
with open(csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Defining header row:
    csv_header = next(csv_reader)
    
    # Defining the other rows:
    for row in csv_reader:

        # Number of votes:
        number_of_votes += 1
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            voting_list.append(1)
        else:
            voting_list[candidate_list.index(row[2])] += 1

# Percent of votes:            
percent_list = [(100/number_of_votes) * x for x in voting_list]

# Determine the winner:
winner = candidate_list[voting_list.index(max(voting_list))]

# Print Analysis:      
print('Election Results')
print('------------------------')
print('Total Votes: ' + str(number_of_votes))
print('------------------------')

for x in candidate_list:
    print(x  +  ':'  +  str(format(percent_list[candidate_list.index(x)], '.3f'))  
         +   '% ('  +  str(voting_list[candidate_list.index(x)])  + ')')
    
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")    