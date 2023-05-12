# Import csv and os modules 
import csv
import os

# Create path for the election data
data_path = os.path.join('Resources', 'election_data.csv')

# Dictionary to set up the candidate and their vote count
# Keys are candidate names and values are their vote count
cand_list = {}

# Variables to store important variables
total_votes = 0
vote_count = []
winner = ["",0]


###########################################################################################
######   This part is where we read the data and extract the important information   ######
###########################################################################################

# Open the data file
with open(data_path) as elec_data:

    # Reads the file
    file_reader = csv.reader(elec_data, delimiter=",")

    header = next(file_reader)  # Skip the header row

    # Loop through the rows of the file
    for row in file_reader:
        
        # Checks if the candidate in the new row already exists in the dictionary
        # If they are, adds 1 to their vote count
        if row[2] in cand_list.keys():
            cand_list[row[2]] +=1
        
        # Adds the candidate in the dictionary if they are not in it with 1 vote
        else:
            cand_list[row[2]] = 1
    
    # Compute total votes by adding all the values for each key (candidate)
    for cand in cand_list.keys():
        total_votes = total_votes + cand_list[cand]

        # Track all the votes for each candidate. This is to check
        vote_count.append([cand, cand_list[cand]])

    # Check for the winner. Compare vote count of 
    for cand in vote_count:
        if cand[1] > winner[1]:
            winner = [cand[0], cand[1]]


    # Print results in the terminal

    print("\n")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

    for cand in vote_count:
        print(f"{cand[0]}: {round(cand[1]/total_votes * 100, 3)}% ({cand[1]})")

    print("----------------------------")
    print(f"Winner: {winner[0]}")
    print("----------------------------")
    

#########################################################################
######   This part is where we write the results into a new file   ######
#########################################################################


result_path = os.path.join("analysis", "results.txt")

with open(result_path, 'w') as result_file:

    # Writes each line exactly how we printed in the terminal
    result_file.writelines(["Election Results \n",
   "---------------------------- \n",
    f"Total Votes: {total_votes} \n",
    "---------------------------- \n"])

    for cand in vote_count:
        result_file.write(f"{cand[0]}: {round(cand[1]/total_votes * 100, 3)}% ({cand[1]}) \n")

    result_file.writelines(["---------------------------- \n",
    f"Winner: {winner[0]} \n",
    "---------------------------- \n"])