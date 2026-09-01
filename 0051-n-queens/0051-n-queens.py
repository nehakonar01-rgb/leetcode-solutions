class Solution:
    def solveNQueens(self, n):

        result = []

        # Create empty chessboard
        board = [["."] * n for _ in range(n)]

        # Keep track of occupied columns and diagonals
        columns = set()
        diagonals1 = set()
        diagonals2 = set()

        def backtrack(row):

            # All queens are placed
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                result.append(solution)
                return

            # Try placing queen in every column
            for col in range(n):

                # Check if column or diagonal is occupied
                if col in columns:
                    continue

                if row - col in diagonals1:
                    continue

                if row + col in diagonals2:
                    continue

                # Place queen
                board[row][col] = "Q"

                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row][col] = "."

                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        backtrack(0)

        return result