import csv

class Employee():
    def __init__(self,id,name,city):
        self.id = id
        self.name = name
        self.city = city

list1 = []
with open('dataset/test2.csv','r') as data:
    value = csv.DictReader(data)
    for item in value:
        emp = Employee(int(item['id']),item['name'],item['city'])
        list1.append(emp)
        
for object in list1:
    print(object.id," ",object.name," ",object.city)
    
