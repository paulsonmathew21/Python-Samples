class Sortness(object):
    def getSortness(self,a):
        self.a=()
        a=list(a)
        n=0
        print a
        for i in range(len(a)):
            l=0
            for j in range(0,i):
                if a[j]>a[i]:
                    #print a[i]
                    #print j
                    l+=1
            for k in range(i,len(a)):
                if a[k]<a[i]:
                  l+=1
            n+=l
            print a[i],l
        #print n
        #s= sum(n[:])
        #print s
        d=float(len(a))
        #print d
        return (n/d)
            #n.append(l+r)
            
        #print n
        #print r
        #print l 
x=Sortness()
print x.getSortness(('32146758'))
                    
			
