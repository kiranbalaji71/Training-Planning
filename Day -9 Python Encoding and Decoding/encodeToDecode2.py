content = 'Hello world everyone'


utf_8 = content.encode("utf-8")
utf_16 = content.encode("utf-16")
utf_32 = content.encode("utf-32")

print('---------------------------------') 
print('utf-8 encode: ',utf_8)
print('utf-8 decode: ',utf_8.decode("utf-8"))
print('---------------------------------')
print('utf-16 encode: ',utf_16)
print('utf-16 decode: ',utf_16.decode("utf-16"))
print('---------------------------------')
print('utf-32 encode: ',utf_32)
print('utf-32 decode: ',utf_32.decode("utf-32"))
print('---------------------------------')