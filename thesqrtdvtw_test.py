class TheSquareDivTwo(object):
    def solve(self,board):
        r=[]
        l=[['.' for x in range(len(board))] for x in range(len(board))]
        for i in range(len(board)):
            count =0
            for j in range(len(board)):
                if board[i][j]=='C':
                    count+=1
            r.append(count)
        #print r
        for i in range(len(l)):
            for j in range(len(l)):
                if len(l)-j-r[i]>0:
                    l[j][i]='.'
                else:
                    l[j][i]='C'
        for i in range(len(l)):
            l[i]=''.join(l[i])
        return l

x=TheSquareDivTwo()
print x.solve(("...CCC","...CCC","...CCC","CCC...","CCC...","CCC..."))
            
