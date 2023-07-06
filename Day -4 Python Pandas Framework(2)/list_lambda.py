number = int(input("Enter the no. of names : "))
name = []

print("Enter the names :")
for item in range(number):
    name.append(input())

chara = input("enter the character : ")

#Using lambda in Comprehension list
finds = lambda name, chara : [x for x in name if chara in x]
print("----result----")
print(finds(name,chara))