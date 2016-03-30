class DiagonalDisproportion(object):
    def getDisproportion(self,matrix):
        matrix= list(matrix)
        r_1=[]
        r_2=[]
        c_1=0
        c_2=0
        print matrix
        k=matrix[::-1]
        for i in range(0,len(matrix)):
            #print i 
            l=matrix[i]
            m=k[i]
            #print k
            #print len(l)
            for j in range(0,len(l)):
                if i==j:
                    r_1.append(l[j])
                    r_2.append(m[j])
        for i in range(len(r_1)):
                       c_1+=int(r_1[i])
                       c_2+=int(r_2[i])
        return c_1-c_2
        #print int(c_1)
        #print int(c_2)
        #print r_1
        #print r_2
        #return matrix                
x=DiagonalDisproportion()
print x.getDisproportion(["123","456","789"])
