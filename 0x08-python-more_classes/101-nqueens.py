#!/usr/bin/python3
""" Solves the N-queens puzzle """


import sys


def init_nboard(n):
    """ Initializes an `n`x`n` sized chessboard with 0's """

    nboard = []
    [nboard.append([]) for index in range(n)]
    [row.append(' ') for index in range(n) for row in nboard]
    return (nboard)


def nboard_dcopy(nboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(nboard, list):
        return list(map(nboard_dcopy, nboard))
    return (nboard)


def get_nlist(nboard):
    """Return the list of lists representation of a solved chessboard."""
    nlist = []
    for m in range(len(nboard)):
        for p in range(len(nboard)):
            if nboard[m][p] == "Q":
                nlist.append([m, p])
                break
    return (nlist)


def x_out(nboard, row, col):
    """ X out spots on a chessboard """
    # X out all forward spots
    for c in range(col + 1, len(nboard)):
        nboard[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        nboard[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(nboard)):
        nboard[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        nboard[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(nboard)):
        if c >= len(nboard):
            break
        nboard[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        nboard[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(nboard):
            break
        nboard[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(nboard)):
        if c < 0:
            break
        nboard[r][c] = "x"
        c -= 1


def n_solve(nboard, row, queens, n_list):
    """Recursively solve an N-queens puzzle"""
    if queens == len(nboard):
        n_list.append(get_nlist(nboard))
        return (n_list)

    for c in range(len(nboard)):
        if nboard[row][c] == " ":
            tmp_nboard = nboard_dcopy(nboard)
            tmp_nboard[row][c] = "Q"
            x_out(tmp_nboard, row, c)
            n_list = n_solve(tmp_nboard, row + 1, queens + 1, n_list)
    return (n_list)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    nboard = init_nboard(int(sys.argv[1]))
    n_list = n_solve(nboard, 0, 0, [])
    for s in n_list:
        print(s)
