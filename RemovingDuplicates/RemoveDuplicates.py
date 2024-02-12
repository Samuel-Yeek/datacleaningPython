import pandas as pd
#this script checks for duplicate rows in a .csv then removes them
original_data = pd.read_csv('RemovingDuplicates\grocery_list_orignal.csv')
print(original_data.head())
new_data = original_data.drop_duplicates()

print(new_data.head())

new_data.to_csv('RemovingDuplicates\grocery_list_no_duplicates.csv')