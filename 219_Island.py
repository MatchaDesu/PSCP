"Island Uses ChatGPT"

def count_islands(grid,rows,cols):
    "count island"
    visited = [[False] * cols for _ in range(rows)]
    #print(visited) เป็นค่าความจริง

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or not grid[r][c] :
            return
        if visited[r][c] :
            return
        visited[r][c] = True
        # ตรวจสอบทั้ง 8 ทิศทาง ระบบพิกัด
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            dfs(r + dr, c + dc)

    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                island_count += 1

    return island_count

def main() :
    "main"
    m, n = map(int, input().strip().split())
    island = []

    for _ in range(m):
        row = list(map(int, input().split()))
        island.append(row)
    print(count_islands(island,m,n))
main()
