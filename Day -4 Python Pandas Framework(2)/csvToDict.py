import csv

detail={}
# key = ['id','name','city']
with open('./dataset/test2.csv','r') as data:
    value = csv.DictReader(data)
    for item in value:
        emp_id = item['id']
        emp_detail = item
        detail[emp_id] = emp_detail

index = int(input("Enter the index number : "))
result = detail[index]
for i in result:
    print(result[i])