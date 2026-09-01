class Solution:
    def totalNQueens(self, n):

        count = [0]

        columns = set()
        diagonals1 = set()
        diagonals2 = set()

        def backtrack(row):

            if row == n:
                count[0] += 1
                return

            for col in range(n):

                if col in columns:
                    continue

                if row - col in diagonals1:
                    continue

                if row + col in diagonals2:
                    continue

                # Place queen
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                backtrack(row + 1)

                # Backtrack
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        backtrack(0)

        return count[0]