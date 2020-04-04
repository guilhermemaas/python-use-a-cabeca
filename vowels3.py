vowels = ['a', 'e', 'i', 'o', 'u']

word_input = (input('Provide a word to search for vowels:')).lower()
word = list(word_input)

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    if v > 0:
        print(k, 'was found', v, 'time(s).')
