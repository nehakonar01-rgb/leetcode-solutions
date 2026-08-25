class Solution:
    def solveSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] != '.':
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        self.backtrack(board, rows, cols, boxes)

    def backtrack(self, board, rows, cols, boxes):

        bestRow = -1
        bestCol = -1
        bestCandidates = None

        # Find empty cell with minimum candidates
        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':

                    box = (r // 3) * 3 + (c // 3)

                    candidates = []

                    for num in '123456789':

                        if (num not in rows[r] and
                            num not in cols[c] and
                            num not in boxes[box]):

                            candidates.append(num)

                    # No possible number
                    if len(candidates) == 0:
                        return False

                    # Best cell so far
                    if (bestCandidates is None or
                        len(candidates) < len(bestCandidates)):

                        bestCandidates = candidates
                        bestRow = r
                        bestCol = c

                        # Only one possibility
                        if len(candidates) == 1:
                            break

            if bestCandidates is not None and len(bestCandidates) == 1:
                break

        # No empty cells
        if bestCandidates is None:
            return True

        box = (bestRow // 3) * 3 + (bestCol // 3)

        for num in bestCandidates:

            # Place
            board[bestRow][bestCol] = num

            rows[bestRow].add(num)
            cols[bestCol].add(num)
            boxes[box].add(num)

            # Recurse
            if self.backtrack(board, rows, cols, boxes):
                return True

            # Undo
            board[bestRow][bestCol] = '.'

            rows[bestRow].remove(num)
            cols[bestCol].remove(num)
            boxes[box].remove(num)

        return False      