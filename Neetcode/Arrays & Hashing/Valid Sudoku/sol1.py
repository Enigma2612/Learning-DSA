class Solution:

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        check = [i for i in range(1,10)]

        #checking 1-9
        for row in board:
            for cell in row:
                if cell == '.':
                    continue
                if int(cell) not in check:
                    return False

        #checking rows
        for row_num, row in enumerate(board):
            dic = {}
            for i in row:
                if i == '.': continue
                dic[i] = dic.get(i, 0) + 1
                if dic[i] > 1:
                    return False
            
        #checking cols
        for col_num in range(len(board[0])):
            dic = {}
            for i in range(len(board)):
                if board[i][col_num] == '.': continue
                dic[board[i][col_num]] = dic.get(board[i][col_num], 0) + 1
                if dic[board[i][col_num]] > 1:
                    return False

        #checking boxes
        boxes = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []
                for k in range(3):
                    box.extend(board[i+k][j:j+3])
                boxes.append(box)
        
        print(boxes)

        for box in boxes: 
            dic = {}
            for i in box:
                if i == '.': continue
                dic[i] = dic.get(i,0) + 1
                if dic[i] > 1:
                    return False
        return True