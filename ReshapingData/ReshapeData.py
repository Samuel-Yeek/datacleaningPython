import pandas as pd

messy = pd.read_csv('ReshapingData/messy_bank_accounts.csv')


clean = pd.melt(messy, id_vars='AccountID', value_vars=['Checking','Savings'],var_name='Account Type', value_name='Balance')


# frame = the dataframe you want to "melt"
# id_vars = the columns(s) you want to keep the same
# value_vars = the column(s) of messy data you want to turn into rows
# var_name = what to call the columns of the new dataframe that stores the values
#var_name = what to call the columns of the new dataframe that stores the variables

clean.to_csv('ReshapingData/clean_bank_accounts.csv', index=False)
#save the cleaned data to a new .csv file.