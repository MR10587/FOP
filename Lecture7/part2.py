def open_file(filename):
    with open(filename, "r") as f:
        data = [int(line) for line in f.read().splitlines()]
        return data

def filtering_list(data):
    max = data[0]
    for number in data:
        if number < max:
            data.remove(max)
        else:
            max = number

    print(data)

filtering_list(open_file("data.txt"))