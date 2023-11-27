text = input('Введите текст: ')
text = text.lower()
punctuation = ['.', ',', '\'', '!', '?', ':', ';', '—']
for symbol in punctuation:
    text = text.replace(symbol, '')
words = text.split()
print(f'Количество разных слов: {len(set(words))}')

for char in punctuation:
    text = text.replace(char, "")

longest_word = words[0]
short_word = words[0]
word_frequency = {}
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(short_word):
        short_word = word
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print('Самое длинное слово:', longest_word)
print('Самое короткое слово:', short_word)
print('Частота слов:')
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")



