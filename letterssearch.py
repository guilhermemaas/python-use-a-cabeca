def search4vowels(word:str) -> set:
    '''Display any vowels found in asked-for word.'''
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
        
        
def search4vowels2(word:str) -> set:
    '''Return a boolean based on any vowels found.'''
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


def search4vowels3(word:str) -> set:
    '''Display any vowels found in asked-for word.'''
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found


def search4vowels4(word:str) -> set:
    '''Display any vowels found in asked-for word.'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters (phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


#print(help(search4vowels4))
#search4vowels(str(input('Provide a word to search for vowels: ')).lower())
#print(search4vowels2(str(input('Provide a word to search for vowels: ')).lower()))
#print(search4vowels3(str(input('Provide a word to search for vowels: ')).lower()))
#texto = search4vowels4(str(input('Provide a word to search for vowels: ')).lower())
#print(texto)
print(search4letters(str(input('phrase: ').lower()), str(input('letters: ').lower())))

l = list() #Lista
d = dict() #Dicionario
s = set() #Conjunto
t = tuple() #Tupla
