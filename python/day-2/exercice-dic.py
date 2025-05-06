list_of_tuples = [("name", "Elie"), ("job", "Instructor")]
dictionary1 = dict(list_of_tuples)
print(dictionary1)

keys = ["CA", "NJ", "RI"]
values = ["California", "New Jersey", "Rhode Island"]
dictionary2 = dict(zip(keys, values))
print(dictionary2)

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = {vowel: 0 for vowel in vowels}
print(vowel_dict)

import string
alphabet = string.ascii_uppercase
alphabet_dict = {i + 1: alphabet[i] for i in range(len(alphabet))}
print(alphabet_dict)
