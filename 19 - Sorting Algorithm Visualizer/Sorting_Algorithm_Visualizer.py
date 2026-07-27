import time


def bubble_sort(arr):

    n = len(arr)

    print("\nOriginal Array:")
    print(arr)

    for i in range(n):

        swapped = False

        print(f"\nPass {i + 1}")

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            print(arr)
            time.sleep(0.3)

        if not swapped:
            break

    print("\nSorting Complete!")
    print("Sorted Array:")
    print(arr)


print("=" * 45)
print("   SORTING ALGORITHM VISUALIZER")
print("=" * 45)

try:

    size = int(input("Enter number of elements: "))

    numbers = []

    for i in range(size):
        value = int(input(f"Element {i + 1}: "))
        numbers.append(value)

    bubble_sort(numbers)

except ValueError:
    print("Please enter valid integers.")