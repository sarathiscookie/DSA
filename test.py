user_data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
user_id = 444

def get_result(data, id):
    left = 0
    right = len(user_data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == id:
            return data[mid]
        elif data[mid] < id:
            left = mid + 1
        else:
            right = mid - 1

    return False

result = get_result(user_data, user_id)

if result:
    print(f"Found user index {result} from {user_data}")
else:
    print("Not found!")