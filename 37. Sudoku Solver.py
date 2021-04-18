def solveSudoku():
    """
        Do not return anything, modify board in-place instead.
        """
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    def find_empty(bo):
        for i in range(9):
            for j in range(9):
                if bo[i][j] == ".":
                    return i, j

    def is_possible(bo, num, n):
        # check row
        for i in range(0, 9):
            if bo[n[0]][i] == str(num) and n[1] != i:
                return False
        # check column
        for i in range(0, 9):
            if bo[i][n[1]] == str(num) and n[0] != i:
                return False
        # check the box
        x0 = n[1] // 3
        y0 = n[0] // 3

        for i in range(y0*3, y0*3 + 3):
            for j in range(x0*3, x0*3 + 3):
                if bo[i][j] == str(num):
                    return False

        return True

    def solve(bo):

        find_next = find_empty(bo)
        if not find_next:
            return True
        else:
            x, y = find_next

        for i in range(1,10):
            if is_possible(bo, i, (x,y)):
                bo[x][y] = str(i)

                if solve(bo):
                    return True

                bo[x][y] = "."

        return False

    def print_board(bo):

        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])

                else:
                    print(bo[i][j] + " ", end="")
        print("")
        print("* * * * * * * * * * * * * * *")
        print("")

    solve(board)
    print_board(board)


if __name__ == '__main__':
    solveSudoku()
