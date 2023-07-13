with open('./textFile/spanish.txt','r',encoding='utf-8') as spfile:
    with open('./textFile/spoutput.txt','w',encoding='utf-16') as spresult:
        spresult.write(spfile.read())

print('spainish file encoding successfully')

with open('./textFile/japanese.txt','r',encoding='utf-8') as jafile:
    with open('./textFile/jaoutput.txt','w',encoding='utf-16') as jaresult:
        jaresult.write(jafile.read())

print('japanese file encoding successfully')