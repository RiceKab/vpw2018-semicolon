def pour(amounts, capacities, from_idx, to_idx):
    remaining = capacities[to_idx] - amounts[to_idx]
    poured_amount = min(amounts[from_idx], remaining)
    amounts[from_idx] -= poured_amount
    amounts[to_idx] += poured_amount


cases = int(input())
for case_nr in range(1, cases + 1):
    bucket_amount = []
    bucket_capacity = []
    for _ in range(int(input())):  # Setup
        bucket = [int(b) for b in input().split(sep=' ')]
        bucket_amount.append(bucket[0])
        bucket_capacity.append(bucket[1])
    for _ in range(int(input())):  # Instructions
        indices = [int(b) for b in input().split(sep=' ')]
        pour(bucket_amount, bucket_capacity, indices[0] - 1, indices[1] - 1)
    print("{}".format(case_nr), end='')
    for amt in bucket_amount:
        print(" {}".format(amt), end='')
    print()
