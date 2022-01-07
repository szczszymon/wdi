def jump(n, moves, board, pos, counter):
    if counter == n**2:
        return True

    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if can_move(new_pos, board, n):
            board[new_pos[0]][new_pos[1]] = counter + 1
            if jump(n, moves, board, new_pos, counter + 1):
                return True
            board[new_pos[0]][new_pos[1]] = 0


def can_move(new_pos, board, n):
    if new_pos[0] not in range(n) or new_pos[1] not in range(n) or board[new_pos[0]][new_pos[1]] != 0:
        return False
    return True


def main():

    moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

    n = int(input("Podaj wymiar szachownicy: "))
    pos = list(input("Podaj wiersz skoczka: ").split(","))

    pos[0], pos[1] = int(pos[0]), int(pos[1])
    board = []

    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)

    board[pos[0]][pos[1]] = 1

    if jump(n, moves, board, pos, 1):
        print("\nMapa drogi skoczka:\n")

        for i in range(n):
            for j in range(n):
                print('{0: >2}'.format(board[i][j]), end=" ")
            print()
    else:
        print("\nSolution doesn't exist")


if __name__ == "__main__":
    main()
