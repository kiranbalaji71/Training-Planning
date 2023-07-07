import requests
import csv

response =requests.get('http://gateway.marvel.com/v1/public/characters?ts=1&apikey=1467466b0302a83cb434374488d240d6&hash=1a5212bd573534299dd0b6f16b8c4d30')

data = response.json()


result = data['data']['results']
with open('./csv_file/marvel_cs.csv','w') as file1:
    csv_data =csv.writer(file1)
    csv_data.writerow(["id","name","modified","image"])
    for i in result:
        csv_data.writerow([i['id'],i['name'],i['modified'],i['thumbnail']['path']+'.jpg'])
print('csv created successfully')