def calculate_pet_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
    return [human_years, cat_years, dog_years]

while True:
    try:
        human_years = int(input("Enter the number of human years (>=1): "))
        if human_years < 1:
            print("Please enter a whole number greater than or equal to 1.")
            continue
        print(calculate_pet_years(human_years))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
