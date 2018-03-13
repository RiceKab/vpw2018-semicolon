"""
Quick note on regex:
re.match(regex, str)    -- match from the start
re.matchfull(...)       -- match from start to end
re.search(...)          -- match anywhere
"""


def flood_fill_count(matrix, visitation_matrix, start_x, start_y, stop_symbol):
    """ Count number of 'tiles' that are enclosed by the given stop_symbol. Must be started on a correct position. """

    def flood_fill_count_recurse(x, y):
        if visitation_matrix[x][y]:
            return 0
        visitation_matrix[x][y] = True
        if matrix[x][y] == stop_symbol:  # Edge hit
            return 0
        # Add self + neighbours
        total = 1
        if x > 0:
            total += flood_fill_count_recurse(x - 1, y)
        if x < len(matrix) - 1:
            total += flood_fill_count_recurse(x + 1, y)
        if y > 0:
            total += flood_fill_count_recurse(x, y - 1)
        if y < len(matrix[x]) - 1:
            total += flood_fill_count_recurse(x, y + 1)
        return total

    return flood_fill_count_recurse(start_x, start_y)


def print_matrix(matrix, padding=0):
    """ Utility function to print row on each line. """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("{:{padding}}".format(matrix[i][j], padding=padding), end='')
        print("")


def transpose(rows):
    """ Returns a transposed version of the matrix. Does not modify given matrix. """
    col_size = len(rows[0])
    transposed = [[row[i] for row in rows] for i in range(col_size)]
    return transposed


# END HELPERS
cases = int(input())
for case_nr in range(cases):
    pass
