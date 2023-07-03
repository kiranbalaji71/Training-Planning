file_path = input("Enter your File PATH : ")
user_input = input("Enter your text : ")

try:
    with open(file_path,'w') as file:
        file.write(user_input)
    print("File name " + file_path +" created successfully")

except Exception as e:
    print("ERROR : Problem with writing file " + str(e))

