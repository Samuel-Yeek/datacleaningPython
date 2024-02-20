import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("AggregatingMultipleFiles\AggregatedExams.csv")

# Create a figure for the subplots
plt.figure(figsize=(12, 6))

# Create the first subplot (bar chart)
plt.subplot(1, 2, 1)
plt.bar(data['Grade'], data['Average test score'])
plt.xlabel('Grade')
plt.ylabel('Average test score')
plt.title('Average Test Score by Grade')

# Create the second subplot (pie chart)
plt.subplot(1, 2, 2)
plt.pie(data['Count'], labels=data['Grade'], autopct='%1.1f%%')
plt.title('Grade Distribution')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plots
plt.show()
