class Solution:
    #set but how?
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                item=board[i][j]
                if item in s:
                    return False
                elif item !='.':
                    s.add(item)
        for i in range(9):
            s=set()
            for j in range(9):
                item=board[j][i]
                if item in s:
                    return False
                elif item !='.':
                    s.add(item)
        for i in range(0,9,3):
            for j in range(0,9,3):
                s=set()
                for x in range(3):
                    for y in range(3):
                        item=board[i+x][j+y]
                        if item in s:
                            return False
                        elif item != '.':
                            s.add(item)
        return True


        