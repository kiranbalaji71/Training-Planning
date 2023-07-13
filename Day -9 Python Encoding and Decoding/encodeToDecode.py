text_file = input('Enter the text file path: ')
output_file = input('Enter the output file path: ')
encode_value = input('Give the encoding type like UTF-8, UTF-16: ')

try:
    with open(text_file,'r',encoding='utf-8') as file:
        with open(output_file,'w',encoding=encode_value) as return_file:
            return_file.write(file.read())
            print('Output file created successfully')

except Exception as e:
    print(e)