with open('./textFile/spanish.txt','r',encoding='utf-8') as spfile:
    with open('./textFile/spoutput.txt','w+',encoding='utf-16') as spresult:
        spresult.write(spfile.read())
        if(spfile.read() == spresult.read()):
            print('spainish file is coming out correctly')
        else:
            print('spanish file is not coming out correctly')

with open('./textFile/japanese.txt','r',encoding='utf-8') as jafile:
    with open('./textFile/jaoutput.txt','w+',encoding='utf-16') as jaresult:
        jaresult.write(jafile.read())
        if(jafile.read() == jaresult.read()):
            print('japanese file is coming out correctly')
        else:
            print('japanese file is not coming out correctly')

with open('./textFile/russian.txt','r',encoding='utf-8') as rufile:
    with open('./textFile/ruoutput.txt','w+',encoding='utf-16') as ruresult:
        ruresult.write(rufile.read())
        if(rufile.read() == ruresult.read()):
            print('russian file is coming out correctly')
        else:
            print('russian file is not coming out correctly')