import os
import csv

csvpath = os.path.join('/Users/eleanorhayden/Documents/GitHub/python-challenge/PyBank/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total_months = 0
    net_total = 0
    current_amount = 0
    previous_amount = 0
    total_change = 0
    change_count = 0
    greatest_increase = 0
    greatest_increase_date = ''
    greatest_decrease = 0
    greatest_decrease_date = ''

    for row in csvreader:
        total_months += 1
        #find Total Months

        current_date = row [0]
        #find date for greatest increase/decrease 

        current_amount = int(row[1])
        net_total += current_amount
        #find net total amount of "Profit/Losses" over entire period

        if previous_amount != 0:
            change = current_amount - previous_amount
            total_change += change
            change_count += 1
        #if the previous amount is not equal to 0, then subtract current amount from previous amount
        #keeps track of change variable as it changes, variable count goes up 1 per change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = current_date
            #if change is greater than current greatest increase value, then update it to change value
            #assigns date to greatest increase date variable to associate increase with date

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = current_date
             #if change is less than current greatest decrease value, then update it to change value
            #assigns date to greatest decrease date variable to associate decreae with date   

        previous_amount = current_amount
        #changes in "Profit/Losses" over the entire period
    average_change = total_change / change_count
    #average of the changes

print("Total Months:", total_months)
print("Total: $", net_total)
print("Average Change: $", average_change)
print("Greatest Increase in Profits:", greatest_increase_date, '($',greatest_increase,')')
print("Greatest Decrease in Profits:", greatest_decrease_date, '($',greatest_decrease,')')