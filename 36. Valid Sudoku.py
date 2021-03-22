class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = (0,1,2,3,4,5,6,7,8)
        col = (0,1,2,3,4,5,6,7,8)
        square = ((0,1,2),(3,4,5),(6,7,8))
        
        def checkRow(board):
            
            for row in board:
                crawler = []
                
                for item in row: 
                    if item == ".":
                        continue
                        
                    elif item not in crawler:
                        crawler.append(item)
                        
                    else:
                        return False
                    
            return True
            
        def checkColumn(board):
            
            for i in col:
                crawler = []
                
                for row in board:
                    item = row[i]
                    if item == ".":
                        continue
                        
                    elif item not in crawler:
                        crawler.append(item)
                        
                    else:
                        return False
                
            return True
        
        def checkSquare(board):
            
            for row in square:
                
                for col in square:
                    is_valid_square = checkFunc(row, col)
                    if not is_valid_square:
                        return False
                    
            return True
        
        def checkFunc(row, col):
            crawler = []
            for i in row:
                
                for j in col:
                    item = board[i][j]
                    if item == ".":
                        continue
                        
                    elif item not in crawler:
                        crawler.append(item)
                        
                    else:
                        return False
                    
            return True
            
        if checkRow(board) and checkColumn(board) and checkSquare(board):
            return True
        
        else:
            return False