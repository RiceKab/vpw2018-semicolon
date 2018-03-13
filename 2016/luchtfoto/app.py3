def flood_fill_count(matrix, visited, row, col):
    def flood_fill_count_recurse(x, y):
        if visited[x][y]:
            return 0
        visited[x][y] = True
        if matrix[x][y] == '.':
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

    return flood_fill_count_recurse(row, col)


cases = int(input())
for case_nr in range(1, cases + 1):
    height = int(input())
    width = int(input())
    visited = []
    matrix = []
    for _ in range(height):
        matrix.append([c for c in input()])
        visited.append([False for _ in range(width)])
    size_results = {}
    # Starting traversal
    for r in range(height):
        for c in range(width):
            if visited[r][c]:
                continue
            if matrix[r][c] == '+':
                island_size = flood_fill_count(matrix, visited, r, c)
                if island_size in size_results:
                    size_results[island_size] += 1
                else:
                    size_results[island_size] = 1
            visited[r][c] = True
    # Output
    print("{}".format(case_nr), end='')
    for size in sorted(size_results.keys()):
        print(" {} {}".format(size, size_results[size]), end='')
    print()
