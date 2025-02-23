import numpy 

class TicTacToe:
    def __init__(self):
        self.grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
        
    def setPixel(self,player:int) -> bool:
        _coords: str = input('Set Your Position: ')
        if not _coords.isdecimal(): return False
        
        if len(_coords) != 2: return False
        
        x , y = int(_coords[1]), int(_coords[0])
        
        if x > len(self.grid[0]) - 1 or y > len(self.grid) - 1: return False
        
        if self.grid[y][x] == 0:
            self.grid[y][x] = player
            return True
        else:
            return False
        
    def checkWin(self) -> bool:
        
        #check for draw
        a,n = 0,0
        for y in self.grid:
            for x in y:
                n += x != 0
                a += 1
        
        if a == n: 
            print("Draw")
            return True
        
        for row in self.grid:
            if self.checkSum(row): return True

        _vert = numpy.rot90(self.grid)
        
        for col in _vert:
            if self.checkSum(col): return True
        
        if self.checkSum([self.grid[i][i] for i in range(len(self.grid))]): return True
        
        if self.checkSum([_vert[i][i] for i in range(len(self.grid))]): return True
        
    def checkSum(self,s) -> bool:
        if sum(s) == 3:
            print('Win P1')
            return True
        if sum(s) == -3:
            print('Win P2')
            return True    
    
    def graphics(self):
        for y in self.grid:
            print("   ")
            for x in y:

                match x:
                    case 1:
                        print(" X ",end='')
                    case -1:
                        print(" O ",end='')
                    case 0:
                        print("   ",end='')
            print("   ")
    
    def update(self) -> None:
        p = (1,-1)
        t = False
        while not self.checkWin():
            print(f'Move: Player {int(t)+1}')
            self.graphics()
            #Graphic Stuff
            legalMove = False
            while not legalMove:
                legalMove = self.setPixel(p[t])
            
            t = not t
TTT = TicTacToe()
TTT.update()