def binary_search(arr, target):                    #Binary Search#
    low = 0 
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


my_numbers = [2,5,8,12,16,23,38,56,72,91]

print(f"List to search: {my_numbers}")

target = 23
result = binary_search(my_numbers, target)
print(f"Looking for {target}...")
print(f"Found at index: {result}\n")

# ///////////////////////////////////////////////////////////



def linear_search(array, target1):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1

numbers = [10,50,30,70,80,60]
target_number = 70
result = linear_search(numbers, target_number)

if result != -1:
    print(f"Success! Number {target_number} found")
else:
    print(f"Number {target_number} is not in the list.")

