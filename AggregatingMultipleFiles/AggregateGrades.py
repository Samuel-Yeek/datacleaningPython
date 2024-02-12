import glob
import pandas as pd

exam_files = glob.glob('AggregatingMultipleFiles/exams*.csv')
# aggregate all the data into a single dataframe

df_list = []
#list for loop

for filename in exam_files:
    df = pd.read_csv(filename)
    df_list.append(df)
all_grades = pd.concat(df_list)
#put all the data into one dataframe


all_grades.to_csv('AggregatingMultipleFiles/AggregatedExams.csv')
#save the aggreagated dataframe to a new .csv file.