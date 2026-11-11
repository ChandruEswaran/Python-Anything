# Progrss of the main execution

from sorting import bubble_sort

from display import (
    display_original,
    display_result
)


def get_numbers():

    print("\n--- Enter Numbers ---")

    try:

        count = int(input("How many numbers? "))

        if count <= 0:

            print("Please enter a positive number!")
            return None

        numbers = []

        for i in range(count):

            value = float(
                input(f"Enter number {i + 1}: ")
            )

            numbers.append(value)

        return numbers

    except ValueError:

        print("Invalid input! Please enter numeric values.")
        return None


def display_menu():

    print("\n")
    print("=" * 50)
    print("          BUBBLE SORT APPLICATION")
    print("=" * 50)

    print("1. Enter Numbers")
    print("2. Display Original Numbers")
    print("3. Sort in Ascending Order")
    print("4. Sort in Descending Order")
    print("5. Exit")

    print("=" * 50)


def main():

    numbers = None

    while True:

        display_menu()

        choice = input("Enter Your Choice (1-5): ").strip()

        if choice == "1":

            numbers = get_numbers()

            if numbers is not None:

                print("\nNumbers saved successfully!")

        elif choice == "2":

            if numbers is None:

                print("Please enter numbers first!")

            else:

                display_original(numbers)

        elif choice == "3":

            if numbers is None:

                print("Please enter numbers first!")
                continue

            sorted_numbers, comparisons, swaps, passes = (
                bubble_sort(numbers, "asc")
            )

            display_result(
                numbers,
                sorted_numbers,
                "Ascending",
                comparisons,
                swaps,
                passes
            )

        elif choice == "4":

            if numbers is None:

                print("Please enter numbers first!")
                continue

            sorted_numbers, comparisons, swaps, passes = (
                bubble_sort(numbers, "desc")
            )

            display_result(
                numbers,
                sorted_numbers,
                "Descending",
                comparisons,
                swaps,
                passes
            )

        elif choice == "5":

            print("\nThank you for using Bubble Sort Application!")
            break

        else:

            print("\nInvalid choice! Please select 1 to 5.")


if __name__ == "__main__":

    main()
