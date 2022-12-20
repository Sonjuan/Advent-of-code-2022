# grid = [list(x) for x in open(0).read().strip().splitlines()]

# for r, row in enumerate(grid):
#     for c, item in enumerate(row):
#         if item == "S":
#             sr = r
#             sc = c
#             grid[r][c] = "a"
#         if item == "E":
#             er = r
#             ec = c
#             grid[r][c] = "z"

# q = []
# q.append([0, sr, sc])
# visited = {(sr, sc)}

# while q :
#     d, r, c = q.pop(0)
#     for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] :
#         if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) :
#             continue
#         if (nr, nc) in visited :
#             continue
#         if ord(grid[nr][nc]) - ord(grid[r][c]) > 1 :
#             continue
#         if nr == er and nc == ec :
#             print(d + 1)
#             exit(0)
#         visited.add((nr, nc))
#         q.append([d+1, nr, nc])

grid = [list(x) for x in open(0).read().strip().splitlines()]

for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

q = []
q.append([0, er, ec])
visited = {(er, ec)}

while q :
    d, r, c = q.pop(0)
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] :
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) :
            continue
        if (nr, nc) in visited :
            continue
        if ord(grid[nr][nc]) - ord(grid[r][c]) < -1 :
            continue
        if grid[nr][nc] == "a" :
            print(d + 1)
            exit(0)
        visited.add((nr, nc))
        q.append([d+1, nr, nc])
