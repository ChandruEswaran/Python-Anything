# Bubble Sort Project

Bubble Sort is a sorting algorithm used to arrange a collection of numbers in ascending or descending order. Sorting is easier to understand when you can watch the numbers move. This interactive project lets you enter a list and compare bubble sort in ascending or descending order.

### How it's work 
It works by comparing two adjacent elements and swapping them if they are in the wrong order.

The algorithm repeatedly performs these comparisons until the list is sorted.

### Input
```
numbers = [45, 12, 78, 23, 9, 56]
```

### Ascending output
```
[9, 12, 23, 45, 56, 78]
```

### Descending output
```
[78, 56, 45, 23, 12, 9]
```

## Project functionalities

We'll develop a console application with these features:

1. Enter numbers manually.
2. Display original numbers.
3. Sort numbers in ascending order.
4. Sort numbers in descending order.
5. Display every sorting pass.
6. Show comparison count.
7. Show swap count.
8. Identify whether the list is already sorted.
9. Display sorting performance.
10. Exit the application.

## What it can do

- Accept a list of numeric values
- Show the original list
- Sort in either direction
- Display comparison, swap, and pass counts

## Understand Bubble Sort logic

Before writing the code, understand how the algorithm works.

```
numbers = [5, 3, 8, 2, 1]
```
We need to sort these numbers in ascending order.

#### Pass 1

| Comparison | Action | List |
|---|---|---|
| 5 and 3 | Swap | 3, 5, 8, 2, 1 |
| 5 and 8 | No swap | 3, 5, 8, 2, 1 |
| 8 and 2 | Swap | 3, 5, 2, 8, 1 |
| 8 and 1 | Swap | 3, 5, 2, 1, 8 |

After Pass 1, the largest number (8) moves to the last position.

#### Pass 2

| Comparison | Action | List |
|---|---|---|
| 3 and 5 | No swap | 3, 5, 2, 1, 8 |
| 5 and 2 | Swap | 3, 2, 5, 1, 8 |
| 5 and 1 | Swap | 3, 2, 1, 5, 8 |

### After Pass 2

```
[3, 2, 1, 5, 8]
```
This process continues until the list is sorted.

#### Final Result

```
[1, 2, 3, 5, 8]
```

## SAMPLE CONSOLE EXECUTION

```
==================================================
          BUBBLE SORT APPLICATION
==================================================
1. Enter Numbers
2. Display Original Numbers
3. Sort in Ascending Order
4. Sort in Descending Order
5. Exit
==================================================

Enter Your Choice (1-5): 1

--- Enter Numbers ---
How many numbers? 5

Enter number 1: 5
Enter number 2: 3
Enter number 3: 8
Enter number 4: 2
Enter number 5: 1

Numbers saved successfully!
```

## Ascending order output

```
Enter Your Choice (1-5): 3

Starting Bubble Sort...
Original List: [5.0, 3.0, 8.0, 2.0, 1.0]

Pass 1
Swapped 3.0 and 5.0
No swap: 5.0 and 8.0
Swapped 2.0 and 8.0
Swapped 1.0 and 8.0
Current List: [3.0, 5.0, 2.0, 1.0, 8.0]

Pass 2
No swap: 3.0 and 5.0
Swapped 2.0 and 5.0
Swapped 1.0 and 5.0
Current List: [3.0, 2.0, 1.0, 5.0, 8.0]

Pass 3
Swapped 2.0 and 3.0
Swapped 1.0 and 3.0
Current List: [2.0, 1.0, 3.0, 5.0, 8.0]

Pass 4
Swapped 1.0 and 2.0
Current List: [1.0, 2.0, 3.0, 5.0, 8.0]
```
### Sorting completed

```
==================================================
              SORTING RESULT
==================================================
Original List : [5.0, 3.0, 8.0, 2.0, 1.0]
Sorting Order : ASCENDING
Sorted List   : [1.0, 2.0, 3.0, 5.0, 8.0]
--------------------------------------------------
Total Comparisons : 10
Total Swaps       : 7
Total Passes      : 4
--------------------------------------------------
Status: Sorting completed successfully.
==================================================
```

## Descending order

#### Choose option 4.

```
Sorted List : [8.0, 5.0, 3.0, 2.0, 1.0]
Sorting Order : DESCENDING
```

# Bubble Sort – Time complexity

Time complexity describes how the algorithm's execution time grows as the number of elements increases.

| Case | Time complexity | Explanation |
|---|---|---|
| Best case | `O(n)` | Already sorted, optimized version |
| Average case | `O(n²)` | Elements require multiple swaps |
| Worst case | `O(n²)` | Reverse sorted list |
| Space complexity | `O(n)` | This implementation creates a copy of the input list |

Without the early-stop optimization, even an already sorted list requires O(n²) comparisons.

> **Important:** Bubble Sort is easy to understand, but it is not efficient for sorting large datasets.

## Testing & Edge Cases
For scripts like sorting or algorithmic tools in this repo, here is how they are tested against various inputs to ensure flawless results:

| Testing Checklist | Test Input | Expected Result |
| :--- | :--- | :--- |
| **Standard Numbers** | `[5, 3, 8, 2, 1]` | `[1, 2, 3, 5, 8]` |
| **Already Sorted** | `[1, 2, 3, 4]` | `[1, 2, 3, 4]` |
| **Reverse Order** | `[9, 7, 5, 3]` | `[3, 5, 7, 9]` |
| **Duplicate Values** | `[5, 5, 2, 2]` | `[2, 2, 5, 5]` |
| **Negative Numbers** | `[-5, 3, -2, 1]` | `[-5, -2, 1, 3]` |
| **Floating Numbers** | `[4.5, 2.3, 1.1]` | `[1.1, 2.3, 4.5]` |

## Run it

From this folder, run:

```bash
python main.py
```

Python 3 is required; no extra packages are needed.
