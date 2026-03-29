class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row Check
        for i in range(9):
            seenvalues_row = []
            for j in board[i]:
                if j not in seenvalues_row:
                    if j!= ".":
                        seenvalues_row.append(j)
                else:
                    return False
        

        #Column Check
        for i in range(9):
            seenvalues = []
            for j in range(9):
                if board[j][i] not in seenvalues:
                    if board[j][i] != ".":
                        seenvalues.append(board[j][i])
                else:
                    return False
                
        
        #Sub-Box Check
        last_indx = 0
        for i in range(1, 10):
            if i % 3 == 0:
                current_board = board[last_indx:i]
                last_indx = i
                
                for col in range(0, 9, 3):
                    seen = set()
                    for row in current_board:
                        for j in range(3):
                            val = row[col + j]
                            
                            if val != '.':
                                if val in seen:
                                    return False
                                seen.add(val)
                
        
        return True

                    


