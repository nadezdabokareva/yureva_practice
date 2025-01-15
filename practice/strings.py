import string

stringFromUser = input('Введите строку \n')
wordFromUser = input("Введите слово для поиска: ")
count = stringFromUser.count(wordFromUser)

print(f"Слово '{wordFromUser}' встречается {count} раз(а) в тексте.")