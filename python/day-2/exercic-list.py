values = [1, 2, 3, 4]
for value in values:
    print(value)

for value in values:
    print(value * 20)

names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)

values = [1, 2, 3, 4, 5, 6]
even_values = [value for value in values if value % 2 == 0]
print(even_values)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_values = [value for value in list1 if value in list2]
print(common_values)

words = ["Elie", "Tim", "Matt"]
reversed_lowercase = [word[::-1].lower() for word in words]
print(reversed_lowercase)

string1 = "first"
string2 = "third"
common_letters = sorted(list(set(string1) & set(string2)))
print(common_letters)

divisible_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print(divisible_by_12)

string = "amazing"
vowels = "aeiou"
no_vowels = [char for char in string if char not in vowels]
print(no_vowels)

result = [[0, 1, 2] for _ in range(3)]
print(result)

structure = [[i for i in range(10)] for _ in range(10)]
print(structure)
