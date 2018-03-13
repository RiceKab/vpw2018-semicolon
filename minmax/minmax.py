count = int(input())
for list_index in range(count):
    numbers = []
    for _ in range(int(input())):
        numbers.append(int(input()))
    print("{} {} {}".format(list_index + 1, min(numbers), max(numbers)))
