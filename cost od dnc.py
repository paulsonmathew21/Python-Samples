class CostOfDancing(object):
    def minimum(self,k,danceCost):
        self.k=k
        self.danceCost=[]
        m=len(danceCost)
        for i in range(0,m):
            for j in range(i+1,m):
                if danceCost[i]>danceCost[j]:
                    t=danceCost[i]
                    danceCost[i]=danceCost[j]
                    danceCost[j]=t
            print danceCost
        return sum(danceCost[:k])                
x=CostOfDancing()
print x.minimum(2,[3,5,2,4])
