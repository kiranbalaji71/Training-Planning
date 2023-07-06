import csv

detail={}
# key = ['id','name','city']
with open('./dataset/test2.csv','r') as data:
    value = csv.DictReader(data)
    for item in value:
        emp_id = item['id']
        detail[emp_id] = item

index = input("Enter the index number : ")
print(detail[index])
