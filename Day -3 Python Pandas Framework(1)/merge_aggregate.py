import pandas as pd

file1 = input("Enter your csv file 1 path: ")
file2 = input("Enter your csv file 2 path: ")
output_file = input("Enter your output csv file path: ")

dataset1 = pd.read_csv(file1)
dataset2 = pd.read_csv(file2)

output = pd.merge(dataset1,dataset2, how='left')

result = output.groupby(['id','emp_name','city'])['performance'].mean()

result.to_csv(output_file)
print("csv file created!!")