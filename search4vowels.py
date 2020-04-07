def search4vowels():
    '''Display any vowels found in asked-for word.'''
    vowels = set('aeiou')
    word = str(input('Provide a word to search for vowels: ')).lower()
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
    
search4vowels()