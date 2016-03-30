class KitayutaMart2(object):
    def numBought(self,K,T):
        i=0
        t=K
        while(t<=T):
            if i==0:
                print K,"1"
                i+=1
                print i,"I1"
            else:
                print K,"2"
                t+=(2**i)*K
                print t,"3"
                i+=1
                print i,"I2"
        return i-1
x=KitayutaMart2()
print x.numBought(160,160)
