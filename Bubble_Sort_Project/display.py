# Works display core

def display_original(numbers):

    print("\n" + "=" * 45)
    print("             ORIGINAL NUMBERS")
    print("=" * 45)

    print("Numbers:", numbers)

    print("=" * 45)


def display_result(
    original,
    sorted_numbers,
    order,
    comparisons,
    swaps,
    passes
):

    print("\n" + "=" * 50)
    print("              SORTING RESULT")
    print("=" * 50)

    print("Original List :", original)
    print("Sorting Order :", order.upper())
    print("Sorted List   :", sorted_numbers)

    print("-" * 50)

    print("Total Comparisons :", comparisons)
    print("Total Swaps       :", swaps)
    print("Total Passes      :", passes)

    print("-" * 50)

    if original == sorted_numbers:

        print("Status: List was already sorted.")

    else:

        print("Status: Sorting completed successfully.")

    print("=" * 50)
