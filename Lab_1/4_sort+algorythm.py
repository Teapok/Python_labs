#--------copy for explain: 12=123456789 3=1 8=123456 1 16=1234567891234 5=123
text = input('Введите текст: ')
words = text.split()
words.sort(key=len, reverse=True)

Bool1, Bool2 = 0, 0

for word in words:
    if Bool1 == 0 and len(word) > 7:
        print('от 7: ', end=' ')
        Bool1 += 1
    elif Bool2 == 0 and 4 <= len(word) <= 7:
        print('\nот 4 до 7: ', end=' ')
        Bool2 += 1
    elif (Bool1 == 1 or Bool2 == 1) and len(word) < 4:
        print('\nостальные: ', end=' ')
        Bool1 += 1
        Bool2 += 1

    print(word, end=' ')