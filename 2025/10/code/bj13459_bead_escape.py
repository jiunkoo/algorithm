#
# @bj app=baekjoon id=13459 lang=python3
#
# [13459] bead escape
#

# @bj code=start
import sys
from collections import deque

input = sys.stdin.readline

def move(x, y, dx, dy, board):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(board, rx, ry, bx, by, N, M):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = set([(rx, ry, bx, by)])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            continue

        for dx, dy in dirs:
            nrx, nry, rc = move(rx, ry, dx, dy, board)
            nbx, nby, bc = move(bx, by, dx, dy, board)

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return 1
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                q.append((nrx, nry, nbx, nby, depth + 1))

    return 0

def main():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    rx = ry = bx = by = -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                bx, by = i, j
                board[i][j] = '.'

    print(bfs(board, rx, ry, bx, by, N, M))

if __name__ == "__main__":
    main()
# @bj code=end
