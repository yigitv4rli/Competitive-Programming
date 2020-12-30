class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row = len(board)
        self.column = len(board[0])
        self.word = word
        self.wordLen = len(word)

        for i in range(self.row):
            for j in range(self.column):
                if self.dfs(board,i,j,0):
                    return True
                    
        return False
                
    
    def dfs(self, board, i, j, index):  
        if index == self.wordLen:
            return True
        if i < 0 or j < 0 or i >= self.row or j >= self.column or board[i][j] != self.word[index]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'
        
        res = self.dfs(board, i+1, j, index+1) or self.dfs(board, i-1, j, index+1) or self.dfs(board, i, j+1, index+1) or self.dfs(board, i, j-1, index+1)
        
        board[i][j] = tmp
        return res
