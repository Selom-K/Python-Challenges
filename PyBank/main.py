# Set Dependencies:
import os
import csv

# Declare Variables:
changes_by_month = []
list_of_months = []
number_of_months = 0
profit_losses = 0
greatest_decrease = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease_month = 0

# Describe the file path to the CSV file:
csv_path = os.path.join('Resources', 'budget_data.csv')

# Opening and reading the file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)
    print(csv_header)
    
    # Setting variables for rows and calculating number 
    # of months and profit, losses:
    previous_row = int(row[1])
    number_of_months += 1
    profit_losses += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Defining headers:
    for row in csvreader:

        # Number of months:                
        number_of_months += 1
        # Determine profit and losses:
        profit_losses += int(row[1])

        # Difference between current month and previous month:
        Difference_between_months = int(row[1]) - previous_row
        changes_by_month.append(Difference_between_months)
        previous_row = int(row[1])
        list_of_months.append(row[0])
        
        # Determining the Greatest Increase:
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Determining the Greatest Decrease:
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Determining the Average:
    average_change = sum(changes_by_month)/ len(changes_by_month)
        
    decrease = min(changes_by_month)
    increase = max(changes_by_month)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${increase})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${decrease})")

