def count_vowels(input_string:str) -> int:
    count = 0
    for el in input_string.lower(): 
        if el in ['a', 'e', 'i', 'o', 'u']: 
            count+=1
    return count

print(f'Number of vowel in input string: {count_vowels(input('Enter string: '))}')