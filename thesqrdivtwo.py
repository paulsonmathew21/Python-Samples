class TheSquareDivTwo(object):
    def solve(self,board):
        r=[]
        l=[['.' for x in range(len(board))] for x in range(len(board))]
        #count =0
        #print board
        for i in range(len(board)):
            count =0
            #l+=[[i]]
            #print l[i]
            #print board[i]
            for j in range(len(board[i])):
                #print board[i][j]
                #l[i][j]=board[i][j]
                if board[i][j]=='C':
                    count+=1
                #l[i]+=board[i][j]
                    #print count
                #else:
                    #print count
            r.append(count)
        for i in range(len(l)):
            for j in range(len(l[i])):
                if (len(l)-r[i]-j)>0:
                    print j,"ddd"
                    l[j][i]='.'
                else:
                    l[j][i]='C'
        for i in range(len(l)):
            l[i]=''.join(l[i])
        print l
        #print board
        return r
x=TheSquareDivTwo()
print x.solve(("...CCC","...CCC","...CCC","CCC...","CCC...","CCC..."))
            
