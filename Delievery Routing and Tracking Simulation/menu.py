# gives user options to look up packages and delivery status
def multiple_choice():
    options = {
        "A":"Run deliveries",
        "B":"Check Status of ALL Packages at a Certain Time",
        "C":"Check Status of ONE Package at a Certain Time.",
        "D":"Exit Program"
    }

    print("Please select how you would like to proceed:")
    for letter, value in options.items():
        print(f"{letter}: {value}")

    user_input = input("Enter the letter of your choice: ").strip().upper()
    return user_input

# plays out what the user picked during multiple choice
def handle_choice(choice):
    if choice == 'A':
        print("Running routing program.....\n")
        mileage1 = run_deliveries(truck1)
        mileage2 = run_deliveries(truck2)
        mileage3 = run_deliveries(truck3)
        total_mileage = mileage1 + mileage2 + mileage3
        total_mileage = round(total_mileage, 2)
        print(f"\nIn total the trucks traveled {total_mileage} miles today.\n")
        user_choice = multiple_choice()
        handle_choice(user_choice)

    if choice == 'B':
        a_input = input("What time would you like to view? (Please input HH:MM am/pm)")
        print_status(a_input)
        user_choice = multiple_choice()
        handle_choice(user_choice)

    elif choice == 'C':
        package_input = input("What package would you like to view?")
        time_input =  input("What time would you like to view this package? (Please input HH:MM am/pm)")
        print_status_package(time_input,package_input)
        user_choice = multiple_choice()
        handle_choice(user_choice)

    elif choice == 'D':
        print("You have choose to exit the program.")

# runs the delivery program
def option_menu():
    print("Welcome to the WGUPS Routing Program!")
    user_choice = multiple_choice()
    handle_choice(user_choice)