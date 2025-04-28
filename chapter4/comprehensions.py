M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

col2 = [row[1] for row in M]

[row[1] + 1 for row in M]
[row[1] for row in M if row[1] % 2 == 0]

diag = [M[i][i] for i in [0, 1, 2]]
doubles = [c * 2 for c in 'hack']

list(range(4))
list(range(−6, 7, 2))

[[x ** 2, x ** 3] for x in range(4)]
[[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]