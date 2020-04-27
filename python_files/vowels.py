prices = []

temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]

words = ['hello', 'world']

car_detail = ['Toyota', 'RAV4', 2.2, 60807]

everything = [prices, temps, words, car_detail]

odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'],
                    ['One', 'Two', 'Three']]

vowels = ['a', 'e', 'i', 'o', 'u']
#word = "Milliways"
word = str(input('Provide a word to search for vowels:'))
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            #print(letter)

for vowel in found:
    print(vowel)
        
"""
>>> nums = [1, 2, 3, 4, 4]
>>> nums.remove(4)
>>> nums
[1, 2, 3, 4]
>>> nums.pop()
4
>>> nums
[1, 2, 3]
>>> nums.pop(0)
1
>>> nums
[2, 3]
>>> nums.pop(3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nums.pop(3)
IndexError: pop index out of range
>>> nums1 = [1, 2, 3, 4]
>>> nums2 = [5, 6, 7, 8]
>>> nums2.extend(nums1)
>>> nums2
[5, 6, 7, 8, 1, 2, 3, 4]
>>> 
>>> 
>>> nums3 = [0, 2]
>>> nums3.insert(1, 2)
>>> nums3
[0, 2, 2]
>>> nums.pop(2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    nums.pop(2)
IndexError: pop index out of range
>>> nums3.pop(1)
2
>>> nums3
[0, 2]
>>> nums.insert(1, 1)
>>> nums3
[0, 2]
>>> nums3.insert(1, 1)
>>> nums3
[0, 1, 2]
>>> nums4 = [1, 2, 3, 4]
>>> nums4.inser(2, "Two-and-a-half")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    nums4.inser(2, "Two-and-a-half")
AttributeError: 'list' object has no attribute 'inser'
>>> nums4.insert(2, "Two-and-a-half")
>>> nums4
[1, 2, 'Two-and-a-half', 3, 4]
>>>

>>> letters.clear()
>>> saying = "Don't Panic!"
>>> letters = list(saying)
>>> letters
['D', 'o', 'n', "'", 't', ' ', 'P', 'a', 'n', 'i', 'c', '!']
>>> letters[0]
'D'
>>> letters[-1]
'!'
>>> letters[3]
"'"
>>> letters[-9]
"'"
>>> first = letters[0]
>>> last = letters[-1]
>>> print(f'primeira: {first}, ultima: {last}'
)
primeira: D, ultima: !

Fatiamento:
>>> letters
['D', 'o', 'n', "'", 't', ' ', 'P', 'a', 'n', 'i', 'c', '!']
>>> letters[0:10:3]
['D', "'", 'P', 'i']
>>> letters[:3]
['D', 'o', 'n']
>>> letters[3:]
["'", 't', ' ', 'P', 'a', 'n', 'i', 'c', '!']
>>> letters[::2]
['D', 'n', 't', 'P', 'n', 'c']
>>> 
"""

