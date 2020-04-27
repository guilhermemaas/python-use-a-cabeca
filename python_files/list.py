prices = []

temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]

words = ['hello', 'world']

car_detail = ['Toyota', 'RAV4', 2.2, 60807]

everything = [prices, temps, words, car_detail]

odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'],
                    ['One', 'Two', 'Three']]

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"

for letter in word:
    if letter in vowels:
        print(letter)
