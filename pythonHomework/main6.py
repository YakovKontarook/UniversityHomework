input_word = input("Введите слово из маленьких латинских букв: ")
vowels = ['a', 'e', 'i', 'o', 'u']

vowels_count = {vowel: 0 for vowel in vowels}
consonants_count = 0

for letter in input_word:
    if letter in vowels:
        vowels_count[letter] += 1
    else:
        consonants_count += 1

print(f"Всего гласных: {sum(vowels_count.values())}, согласных: {consonants_count}")

for vowel, count in vowels_count.items():
    if count == 0:
        print(f"Буква '{vowel}' не встречается в слове: {False}")
    else:
        print(f"Буква '{vowel}' встречается {count} раз(а)")

