# Array should be in sorted order (ascending or descending) otherwise binary search will not work.

user_data = [22, 33, 44, 55, 66, 77, 88, 99]
user_input = 33

def user(arr, input):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (right + left) // 2

        if input == arr[mid]:
            return arr[mid]
        elif input < arr[mid]:
            right = mid - 1
        elif input > arr[mid]:
            left = mid + 1

    return False

if user(user_data, user_input):
    print(f"Found a user {user(user_data, user_input)} in array {user_data}")