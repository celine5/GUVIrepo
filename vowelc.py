original =input('Enter a character:')
character= original.lower()
first =character[0]

if len(original) > 0 and original.isalpha():
    if first in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print ("invalid")
