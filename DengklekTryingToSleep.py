class DengklekTryingToSleep(object):
    def minDucks(self,ducks):
        a=max(ducks)
        b=min(ducks)
        C=[]
        l=[i for i in range(b,a)]
        print l
        for i in l:
            print i
            if i not in ducks:
                C.append(i)
        return C
x=DengklekTryingToSleep()
print x.minDucks((3,5))
