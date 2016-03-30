class WhiteCells(object):
    def countOccupied(self,board):
        self.board=""
        count=0
        #board=list(board)
        for i in range(len(board)):
            c_1=board[i]
            #c_1=list(c_1)
            if i%2==0:
                for j in range(0,len(c_1),2):
                    if c_1[j]=='F':
                        count+=1
            else:
                for j in range(1,len(c_1),2):
                    if c_1[j]=='F':
                        count+=1
        return count
        #print "count is %d"%count
                    #print c_1
                    #print c_1[j]
                    #print board[i]
        print ""
        for i in range(len(board)):
            if i%2!=0:
                print board[i]
            
x=WhiteCells()
print x.countOccupied(("FFFFFFFF","........","........","........","........","........","........","........"))
