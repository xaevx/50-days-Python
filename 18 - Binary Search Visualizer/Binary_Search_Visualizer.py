def binary_search(arr, target):

    left = 0
    right = len(arr) - 1
    step = 1

    while left <= right:

        mid = (left + right) // 2

        print(f"\nStep {step}")
        print(f"Left  : {left}")
        print(f"Right : {right}")
        print(f"Middle: {mid}")
        print(f"Checking Value: {arr[mid]}")

        if arr[mid] == target:
            print(f"\n{target} found at index {mid}.")
            return

        elif arr[mid] < target:
            print(f"{target} is greater than {arr[mid]}. Searching Right Half...")
            left = mid + 1

        else:
            print(f"{target} is smaller than {arr[mid]}. Searching Left Half...")
            right = mid - 1

        step += 1

    print(f"\n{target} not found in the list.")


numbers = []

print("=" * 45)
print("      BINARY SEARCH VISUALIZER")
print("=" * 45)

try:

    size = int(input("How many numbers? "))

    print("\nEnter numbers in ascending order:")

    for i in range(size):
        numbers.append(int(input(f"Number {i + 1}: ")))

    target = int(input("\nEnter number to search: "))

    binary_search(numbers, target)

except ValueError:
    print("Please enter valid integers.") 