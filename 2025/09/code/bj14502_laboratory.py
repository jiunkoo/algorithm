#
# @bj app=baekjoon id=14502 lang=python3
#
# [14502] laboratory
#

# @bj code=start
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty, virus = [], []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread(board):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))

def safe_area(board):
    return sum(row.count(0) for row in board)

answer = 0
for walls in combinations(empty, 3):
    new_lab = [row[:] for row in lab]
    for x, y in walls:
        new_lab[x][y] = 1
    spread(new_lab)
    answer = max(answer, safe_area(new_lab))

print(answer)
# @bj code=end
