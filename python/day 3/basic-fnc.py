def add_two_numbers(a, b):
    return a + b

def greet(name):
    print(f"Hello, {name}!")

def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def sum_list(numbers):
    return sum(numbers)

def print_days():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days:
        print(day)

def check_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

def repeat_word(word, times):
    for _ in range(times):
        print(word)




a = int(input("Enter first number for addition: "))
b = int(input("Enter second number for addition: "))
print(add_two_numbers(a, b))

name = input("Enter a name to greet: ")
greet(name)

num = int(input("Enter a number to check even or odd: "))
check_even_odd(num)

nums_input = input("Enter numbers separated by spaces to sum: ")
nums_list = list(map(int, nums_input.split()))
print(sum_list(nums_list))

print_days()

num_sign = int(input("Enter a number to check if positive, negative, or zero: "))
check_sign(num_sign)

word = input("Enter a word to repeat: ")
times = int(input("Enter how many times to repeat the word: "))
repeat_word(word, times)
