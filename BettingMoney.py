class BettingMoney(object):
    def moneyMade(self,amounts,centsPerDollars,finalResult):
        total=0
        s=0
        x=centsPerDollars[finalResult]*amounts[finalResult]
        print x
        for i in range(len(amounts)):
            if i!=finalResult:
                s+=amounts[i]
        s=s*100
        print s
        return s-x
x=BettingMoney()
print x.moneyMade((10,20,30),(20,30,40),(1))
