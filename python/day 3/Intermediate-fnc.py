def find_largest(numbers):
    return max(numbers)

def check_letter(word, letter):
    return letter in word

def count_to_number(number):
    for i in range(1, number + 1):
        print(i)

nums_input = input("Enter numbers separated by spaces: ")
nums_list = list(map(int, nums_input.split()))
print("Largest number:", find_largest(nums_list))

word = input("Enter a word: ")
letter = input("Enter a letter to check: ")
print("Letter found:", check_letter(word, letter))

num = int(input("Enter a number to count to: "))
count_to_number(num)
