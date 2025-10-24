from re import*


text=input('Введите текст ')

pattern_of_word_in_Russian_English=r'(?:[A-Z]*[a-z]*[А-Я]*[а-я]*){1,}'

Words={}

for word in findall(pattern_of_word_in_Russian_English,text):
    if word not in Words and word!='':
        Words[word]=1
    elif word!='':
        Words[word]+=1

print(Words)
slova_spisok=[]

for k,v in Words.items():
    slova_spisok.append({k:v})

dlina_slovara=len(slova_spisok)

for i in range(dlina_slovara):

    for slovar_sravnim in slova_spisok:
        slovar_max_elem=slova_spisok[i]

        for k,v in slovar_sravnim.items():
            key2,element_sravnim=k,v

        for k,v in slovar_max_elem.items():
            key1,max_elem=k,v

        index_max=slova_spisok.index(slovar_max_elem)
        index_now=slova_spisok.index(slovar_sravnim)
        
        if max_elem<element_sravnim and index_now>index_max:
            max_elem=element_sravnim
            
            slova_spisok[index_max],slova_spisok[index_now]=slova_spisok[index_now],slova_spisok[index_max]    

flag_dla_slov=0

print("Топ 5 самых встречающихся слов:")

while flag_dla_slov<5 and flag_dla_slov<dlina_slovara:
    for k,v in slova_spisok[flag_dla_slov].items():
        print("Слово:",k,"Сколько раз встречается:",v)
    
    flag_dla_slov+=1
