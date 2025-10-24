text=input('Введите текст ')

text+=' '

revers_text_in_symbols=''

for symbol in text:
    revers_text_in_symbols=symbol+revers_text_in_symbols

list_of_words=[]

word_of_text=''

for symbol in text:
    if symbol==' ' and word_of_text!='':
        list_of_words.append(word_of_text)

        word_of_text=''
    else:
        if word_of_text!=' ':
            word_of_text+=symbol

revers_text_in_words=''

for word in list_of_words:
    revers_text_in_words=word+' '+revers_text_in_words


print('Строка в обратном порядке символов ',revers_text_in_symbols)
print('Строка в обратном порядке слов ',revers_text_in_words)