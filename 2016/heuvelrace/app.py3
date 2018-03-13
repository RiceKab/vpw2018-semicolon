points = [25, 100, 500, 1000]


def clamp(min_val, value, max_val):
    return min(max_val, max(min_val, value))


cases = int(input())
for case_nr in range(1, cases + 1):
    jumps = int(input())
    durations = [int(d) for d in input().split(sep=' ')]
    total = 0
    for dur in durations:
        total += clamp(0, dur, 4) * points[0]
        total += clamp(0, dur - 4, 4) * points[1]
        total += clamp(0, dur - 8, 4) * points[2]
        total += clamp(0, dur - 12, 999) * points[3]
    print("{} {}".format(case_nr, total))
