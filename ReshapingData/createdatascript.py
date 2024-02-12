import csv
import random
import itertools

# Generate random account data
data = []
for i in range(1, 101):  # Generate 100 accounts
    account_id = i
    checking_balance = random.randint(-57, 1000)
    savings_balance = random.randint(-57, 25000)
    data.append([account_id,checking_balance, savings_balance])

# Write data to CSV file
with open('ReshapingData/messy_bank_accounts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['AccountID','Checking', 'Savings'])  # Write header
    writer.writerows(data)
