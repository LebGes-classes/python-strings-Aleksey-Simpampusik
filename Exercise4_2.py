text=input('Bведите текст ')

Max_element=0
length_of_word=0

for symbol in text:
    if (symbol==' ' or symbol==',' or symbol=='.') and length_of_word<=20:
        if Max_element<length_of_word:
            Max_element=length_of_word

        length_of_word=0
    
    else:
        if length_of_word>20:
            length_of_word=0
        else:
            length_of_word+=1

K=Max_element

Small_Bukvi='abcdefghijklmnopqrstvuwxyz'
Big_Bukvi='ABCDEFGHIJKLMNOPQRSTVUWXYZ'

for i in range(len(text)):
    if text[i] in Big_Bukvi:
        index_bukvi=Big_Bukvi.index(text[i])

        index_bukvi+=K

        if index_bukvi>25:
            index_bukvi-=25

        text=text[:i]+Big_Bukvi[index_bukvi]+text[i+1:]
    elif text[i] in Small_Bukvi:
        index_bukvi=Small_Bukvi.index(text[i])

        index_bukvi+=K

        if index_bukvi>25:
            index_bukvi-=25

        text=text[:i]+Small_Bukvi[index_bukvi]+text[i+1:]
    
print(text,Max_element)