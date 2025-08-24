user_data = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(len(user_data)):
    min_index = i

    for j in range(i+1, len(user_data)):
        if user_data[j] < user_data[min_index]:
            min_index = j

            print(min_index)


34 < 64
25 < 34
12 < 25
