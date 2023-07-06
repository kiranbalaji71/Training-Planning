import pandas as pd

df = pd.read_csv('./dataset/test.csv')


print("\n--------------------------------------------\n")

print("Aggergate Function")
print("Number of employee : ",df.id.count())
print("Sum of salary : ",df.salary.sum())
print('Average salary of all member : ',df.salary.mean())
print("Young member age : ",df.age.min())
print("Elder member age : ",df.age.max())

print("\n--------------------------------------------\n")

print("Groupby Function")
print(df.groupby('department').mean()[['salary','age']])
print(df.groupby('department').count()[['salary']])

print("\n--------------------------------------------\n")

print("Unique Function")
print(df.position.unique())

print("\n--------------------------------------------\n")

print("Filter Columns and Rows")
print(df.loc[:5,['emp_name','city','age']])

print("\n--------------------------------------------\n")

print("Check like NULL")
print(df[df.age.isnull()])

print("\n--------------------------------------------\n")

print("Number range")
print(df[df.age.between(24,26)])

print("\n--------------------------------------------\n")

print("Using Regex print email ends with Gmail.com")
print(df[df.email.str.contains(r'[@gmail.com]$')])

print("\n--------------------------------------------\n")