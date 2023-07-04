import csv
import json

csv_file_path = input("Enter your csv file path : ")
json_file_path = input("Enter your json file path :")
json_data = []

try:
    with open(csv_file_path,'r') as csvF:
        csvValue = csv.DictReader(csvF)
        for object in csvValue:
            json_data.append(object)

except Exception as e:
    print("Error happen in csv path : " + str(e))

try:
    with open(json_file_path,'w') as jsonF:
        jsonObject = json.dumps(json_data, indent=4)
        jsonF.write(jsonObject)
        print("File created successfully")
        
except Exception as e:
    print("Error happen in json path : " + str(e))
    