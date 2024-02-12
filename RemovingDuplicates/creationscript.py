import csv

#creation script to create a .csv file with the grocery list that has a duplicate
grocery_list = [
    ["Apple", 1.99],
    ["Banana", 0.99],
    ["Orange", 0.79],
    ["Apple", 1.99],
    ["Grapes", 2.49],
    ["Banana", 0.99]
]

# Define the file path
file_path = "RemovingDuplicates/grocery_list_orignal.csv"

# Write the grocery list to the .csv file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Food", "Price"])  # Write the header
    writer.writerows(grocery_list)  # Write the grocery list

print("Grocery list created successfully!")