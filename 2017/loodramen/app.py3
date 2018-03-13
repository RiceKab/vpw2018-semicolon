cases = int(input())


def pprint_window(rows):
    print("-----------------")
    for row in rows:
        print(row)


def transpose(rows):
    col_size = len(rows[0])
    transposed_characters = [[row[i] for row in rows] for i in range(col_size)]
    return transposed_characters
    # cols = [''.join(col) for col in transposed_characters]
    # return cols


def find_seam_index(lines):
    for idx in range(len(lines)):
        if len(lines[idx]) == lines[idx].count('*'):
            return idx
    return -1


def find_seams(rows, row_value=0, col_value=0):
    """pprintWindow(rows)
    print(rowValue, colValue)
    print("-----")"""
    row_idx = find_seam_index(rows)
    if row_idx < 0:  # no seam in this section
        return ""
    cols = transpose(rows)
    col_idx = find_seam_index(cols)
    up = rows[:row_idx]
    top_left = [r[:col_idx] for r in up]
    top_right = [r[col_idx + 1:] for r in up]
    down = rows[row_idx + 1:]
    bottom_left = [r[:col_idx] for r in down]
    bottom_right = [r[col_idx + 1:] for r in down]
    subSeams = "[{0}][{1}][{2}][{3}]".format(  # Numbering makes it easier to read
        find_seams(top_left, row_value, col_value),
        find_seams(top_right, row_value, col_idx + 1),
        find_seams(bottom_left, row_idx + 1, col_value),
        find_seams(bottom_right, row_idx + 1, col_idx + 1)
    )
    return "({},{}){}".format(row_value + row_idx + 1, col_value + col_idx + 1, subSeams)


for case in range(cases):
    rows, cols = [int(el) for el in input().split()]
    window = []
    for n in range(rows):
        window.append(input())
    print("<{},{}>{}".format(rows, cols, find_seams(window)))
