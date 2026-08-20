ch = input().strip()

def has_vowel(ch):
    vowels = 'aeiouAEIOU'
    return ch in vowels

print(str(has_vowel(ch)).lower())
