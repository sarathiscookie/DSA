user_data = [41, 21, 32, 67, 98, 54]
user_input = 33

def find_user_data():
    for data in range(len(user_data)):
        if user_data[data] == user_input:
            print(f"Found user: {user_data[data]}")
            return True

    print(f"Not Found user: {user_input}")
    return False

find_user_data()