# Import csv and os modules 
import csv
import os

# Create path for the budget data
data_path = os.path.join('Resources', 'budget_data.csv')

# Define the important variables in data

net_profit = 0       #Net total profit/loss
average_change = 0   #Average change in profit/loss
gr_inc = ["", 0]     #Stores row for greatest increase in profit
gr_dec = ["", 0]     #Stores row for greatest decrease in profit



###########################################################################################
######   This part is where we read the data and extract the important information   ######
###########################################################################################



with open(data_path) as bank_data:

    file_reader = csv.reader(bank_data, delimiter=',')

    next(file_reader)  #Skip the header row

    prev_row = ["", 0]      #Tracks the previous row. Initial value is just empty
    cur_change = 0          #Change of current row in the loop
    av_change_col = []      #Collection of all the average changes

    for row in file_reader:
        net_profit = net_profit + int(row[1])        #Add the profit/loss from this row
                                                     #to the total net profit/loss

        cur_change = int(row[1]) - int(prev_row[1])  #Calculates the change from this
                                                     #row from previous row profit/losses

        av_change_col.append(cur_change)             #Appends the current change to the 
                                                     #list of all previous changes


        # Comparing if the current change is greater than the previous greatest increase
        # and replaces the greatest increase with the new one including the date
        if cur_change > gr_inc[1]:
            gr_inc = [row[0], cur_change]


        # Comparing if the current change is greater than the previous greatest decrease
        # and replaces the greatest decrease with the new one including the date
        if cur_change < gr_dec[1]:
            gr_dec = [row[0], cur_change]


        # Set the previous row to the curent row for the next iteration in the loop
        prev_row = row


    # Calculate the average change of all the profit/loss 
    for change in av_change_col:
        average_change = average_change + change
    
    average_change = average_change / len(av_change_col) 


    # Printing out the results in the terminal

    print("\n")
    print("Financial Analysis \n")
    print("---------------------------- \n")
    print(f"Total Months: {len(av_change_col)}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest increase in Profit: {gr_inc[0]} (${gr_inc[1]})")
    print(f"Greatest decrease in Profit: {gr_dec[0]} (${gr_dec[1]})")



#########################################################################
######   This part is where we write the results into a new file   ######
#########################################################################


result_path = os.path.join("analysis", "results.txt")

with open(result_path, 'w') as result_file:

    # Writes each line exactly how we printed in the terminal
    result_file.writelines(["Financial Analysis \n", "\n"
     "---------------------------- \n", "\n"
    f"Total Months: {len(av_change_col)} \n",
    f"Total: ${net_profit} \n",
    f"Average Change: ${average_change} \n",
    f"Greatest increase in Profit: {gr_inc[0]} (${gr_inc[1]}) \n",
    f"Greatest decrease in Profit: {gr_dec[0]} (${gr_dec[1]}) \n"])
