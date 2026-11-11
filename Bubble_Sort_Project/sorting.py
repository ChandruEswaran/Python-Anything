
def bubble_sort(numbers, order="asc"):

    # Create a copy to preserve original list
    arr = numbers.copy()

    n = len(arr)

    comparisons = 0
    swaps = 0
    passes = 0

    print("\nStarting Bubble Sort...")
    print("Original List:", arr)

    # Outer loop controls the number of passes
    for i in range(n - 1):

        swapped = False
        passes += 1

        print(f"\nPass {passes}")

        # Inner loop compares adjacent elements
        for j in range(n - i - 1):

            comparisons += 1

            if order == "asc":

                condition = arr[j] > arr[j + 1]

            else:

                condition = arr[j] < arr[j + 1]

            if condition:

                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swaps += 1
                swapped = True

                print(
                    f"Swapped {arr[j]} and {arr[j + 1]}"
                )

            else:

                print(
                    f"No swap: {arr[j]} and {arr[j + 1]}"
                )

        print("Current List:", arr)

        # Stop early if no swapping happened
        if not swapped:

            print("\nList is already sorted!")
            break

    return arr, comparisons, swaps, passes
