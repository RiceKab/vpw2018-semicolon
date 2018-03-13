cases = int(input())

for case in range(cases):
    count = 0
    highest = 0
    next = int(input())
    while next > 0:
        count += 1
        if highest < next:
            highest = next
        next = int(input())
    estimate = round(((count + 1) * highest / count) - 1)
    print("{} {}".format(case + 1, estimate))
