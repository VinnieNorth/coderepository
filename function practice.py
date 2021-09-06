


def duplicates():
    data.sort()
    for i in range(len(data)):
        if i == data[len(data)-1]:
            count = (data.count(data[i]))
            print(f'The number {data[i]} came up in the list {count} times. ')
        elif data[1] == data[i+1]:
            continue
        elif data[i] != data[i+1]:
            count = (data.count(data[i]))
            print(f'The number {data[i]} came up in the list {count} times. ')


data = [1, 5, 9, 8, 3, 3, 4, 0, 1, 3]

duplicates()