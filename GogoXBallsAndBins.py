import itertools
class GogoXBallsAndBins(object):
    def solve(self,T,moves):
        T=list(T)
        print T
        t=list(T)
        result = []
        count=0
        t=t[::-1]
        #for i in range(0,len(T)-1):
            #print T[i],"next"
            #for j in range(i+1,len(T)):
                #if T[j]>T[i]:
                    #print T[j],"fgf"
                    #temp=T[i]
                    #T[i]=T[j]
                    #T[j]=temp
                    #count+=1
                    #print "T",T[i]
                    #print "Tj",T[j]
                #print T
        for i in range(0,len(T)/2):
            count+=abs(T[i]-T[len(T)-1-i])
        return count
            #count+=abs(T[i]-i-T[len(T)-1])
            
            
        #for e in itertools.permutations(T):
            #e=list(e)
            #count+=1
            #print e,"permutation"
            #for i in range(len(e)):
                #if e[i]==t[i]:
                    #if i==0:
                        
                    #result.append(e[i])
                    #print result,"i",i
                #else:
                    #print e[i], t[i]
        #print "count",count   
        
        #return t,T    
x=GogoXBallsAndBins()
print x.solve((1, 2, 3, 4, 5, 6, 7, 8),3)
