numbers = []

# Write a program that user to keep entering the positive number or type done to exit the program
while True:
    value = input("Enter a positive number (or 'done' to finish): ").strip() # remove trailing before and after characters from string

    if value.lower() == "done":
        break

    try:
        n = int(value)
        if n < 0:
            print("Please enter a positive integer.")
            continue
    except ValueError:
        print("That isn’t a valid whole number.")
        continue

     # As long as the User keeps adding a positive number, we want the program to collect numbers and put them in a list
    numbers.append(n)

     # we want the program to check for first even number and print that number, otherwise it should print no even numbers found
    for num in numbers:
        if num % 2 == 0:
            print(f"First even number so far: {num}")
            break
    else:                                    # runs only if the loop finds no even
        print("No even numbers found so far.")

# once the user has decided to exit the program, we want the program to print all the numbers entered by the User
if numbers:
    print("\nAll the numbers you entered:", numbers)
else:
    print("\nYou didn’t enter any numbers.")
