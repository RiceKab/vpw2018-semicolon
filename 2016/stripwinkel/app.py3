import bisect


def pprint_inventory(inv):
    start_idx = curr_idx = 0
    start_element = prev_element = curr_element = inv[curr_idx]
    while curr_element == prev_element + 1 or curr_element == prev_element:
        curr_idx += 1
        prev_element = curr_element
        curr_element = inv[curr_idx]
    print(inv)


cases = int(input())
for caseNr in range(1, cases+1):
    inventoryInput = [e for e in input().split(sep=' ')]
    inventory = [int(item) for item in inventoryInput[1:]]
    inventory = sorted(inventory)
    transactionsInput = [e for e in input().split(sep=' ')]
    transactions = [int(t) for t in transactionsInput[1:]]
    print("{} ".format(caseNr), end='')
    pprint_inventory(inventory)
    for transaction in transactions:
        if transaction > 0:
            bisect.insort_left(inventory, transaction)
            # inventory.append(transaction)
            # inventory = sorted(inventory)
        else:
            item = abs(transaction)
            inventory.remove(item)
        print("{} ".format(caseNr), end='')
        pprint_inventory(inventory)

print('Expected output')
print('''1 2-5 7-9 20-22
1 2-5 7-9 20-22
1 2-5 7-9 20-22
1 2-5 7-9 20-22
1 2-5 7-9 20-22
1 2-9 20-22
1 2-9 12 20-22
1 1-9 12 20-22
1 1 2 4-9 12 20-22
1 1 2 4-9 12 20-22
1 1 2 4-9 12 20-22 24
1 1 2 4-9 12 20-24
// Test case 2 here''')