#191 Write a python program to check if a string contains only uppercase letters.
'''def is_upper(s):
    return s.isupper()
s=input("Enter the string:")

if is_upper(s):
    print("the string only contains uppercase letters")
else:
    print("the stirng does not contains only uppercase letters")'''


#192 Write a python program to check if a string contains only lowercase letters.
'''def is_lower(s):
    return s.islower()
s=input("Enter the string:")

if is_lower(s):
    print("the string only contains lowercase letters")
else:
    print("the stirng does not contains only lowercase letters")'''

#193 Write a python program to check if string contains only whitespace.

'''def is_space(s):
    return s.isspace()
s=input("Enter the string:")
if is_space(s):
    print("the string only contains whitespaces")
else:
    print("the stirng doesn't contain whitespace only")'''

#194 Write a python program to check if a string contians only special characters.
'''def is_special(s):
    for ch in s:
        if ch.isalnum() or ch.isspace():
            return False
    return True

s = input("Enter the string: ")

if is_special(s):
    print("String contains only special characters")
else:
    print("String does not contain only special characters")'''

#195 Write a python program to check if string contsins both letters and digits.
'''def letters_digits(s):
    has_letter=False
    has_digit=False
    for ch in s:
        if ch.isalpha():
            has_letter=True
        if ch.isdigit():
            has_digit=True
    return has_letter and has_digit
s=input("Enter the stirng:")
if letters_digits(s):
    print("the stirng contains both letters and digits")
else:
    print("the stirng does contains both letters and digits")'''

#196 Write a python program to check if a string contains both uppercase and lowercase letters.
'''def lower_upper(s):
    has_upper=False
    has_lower=False
    for ch in s:
        if ch.isupper():
            has_upper=True
        if ch.islower():
            has_lower=True
    return has_upper and has_lower
s=input("Enter the stirng:")
if lower_upper(s):
    print("the stirng contains both uppercase and lowercase letters.")
else:
    print("the stirng does not contains both uppercase and lowercase letters.  ")'''

#197 Write a python program to check if a string contains both vowels and consonants.

'''def vowels_conso(s):
    vowels='aeiouAEIOU'
    has_vowel=False
    has_consonant=False
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                has_vowel=True
            else:
                has_consonant=True
    return has_vowel and has_consonant
s=input("Enter the stirng:")
if vowels_conso(s):
    print("the stirng contains both both vowels and consonants.")
else:
    print("tthe stirng doesn't contains both both vowels and consonants.  ")'''

#198 Write a python program to check if a string contains repeated characters.
'''s = input("Enter string: ")

freq = {}

for ch in s:
    if ch!='':
      if ch in freq:
        freq[ch] += 1
      else:
        freq[ch] = 1

for ch in freq:
    if freq[ch] > 1:
        print(ch, end=" ")'''

#199 Write a python program to check if a string contains unique characters.
'''s = input("Enter string: ")

freq = {}

for ch in s:
    if ch!='':
      if ch  in freq:
        freq[ch] += 1
      else:
        freq[ch] = 1

for ch in freq:
    if freq[ch] <= 1:
        print(ch, end=" ")'''

#200 Write a python program to check if a string contains all vowels.
'''s=input("Enter the stirng:")
vowels='aeiouAEIOU'
for v in vowels:
    if v in vowels:
        print("the string contians all vowels")
        break
    else:
        print("the does not contains all vowels")
        break'''


