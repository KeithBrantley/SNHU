def main():
    # Get current datetime

    import datetime
    current_year = datetime.date.today().year

    # Prompt the user for their name and age
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # Calculate the birth year
    birth_year = current_year - int(age)

    # Print
    print(f"\nHello {name}! You were born in {birth_year}.")

if __name__ == '__main__':
    main()