class GridGenerator(object):
    def generate(self,row,col):
        #a=[]
        #row=list(row)
        #print row
        #a.append(row)
        #a.append(col)
        #a=list(a)
        #print a
        Matrix = [[0 for x in range(len(row))] for x in range(len(row))]
        for i in range(0,len(row)):
            Matrix[i][0]=row[i]
            Matrix[0][i]=col[i]
        for i in range(1,len(Matrix)):
            for j in range(1,len(Matrix[i])):
                #temp1=int(Matrix[i-1][j-1])
                #temp2=int(Matrix[i-1][j])
                #temp3=int(Matrix[i][j-1]
                Matrix[i][j]=int(Matrix[i-1][j-1])+int(Matrix[i-1][j])+int(Matrix[i][j-1])
            print Matrix
        return Matrix[len(Matrix)-1][len(Matrix)-1]
            #print ""
x=GridGenerator()
print x.generate(('10341'),('14103'))
    
