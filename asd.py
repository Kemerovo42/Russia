word = input("Введите какое-нибудь слово")
count = 0
letters = "уУеЕыЫаАоОэЭяЯиИ"
for i in word:
    if i in letters:
        count += 1
print("В слове", word, count ,"гласных букв(ы)")
