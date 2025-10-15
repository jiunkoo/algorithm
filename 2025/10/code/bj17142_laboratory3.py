#
# @bj app=baekjoon id=17142 lang=python3
#
# [17142] laboratory3
#

# @bj code=start
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

virus = []
zeros = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus.append((i, j))
        elif grid[i][j] == 0:
            zeros += 1

if zeros == 0:
    print(0)
    sys.exit(0)

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(active):
    q = deque()
    dist = [[-1]*N for _ in range(N)]

    for x, y in active:
        q.append((x, y))
        dist[x][y] = 0

    remain = zeros
    max_time = 0

    while q:
        x, y = q.popleft()
        t = dist[x][y]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if grid[nx][ny] == 1 or dist[nx][ny] != -1:
                continue

            dist[nx][ny] = t + 1
            if grid[nx][ny] == 0:
                remain -= 1
                max_time = t + 1
                if remain == 0:
                    return max_time
            q.append((nx, ny))
    return float('inf')

answer = float('inf')
for active in combinations(virus, M):
    answer = min(answer, bfs(active))

print(answer if answer != float('inf') else -1)
# @bj code=end
