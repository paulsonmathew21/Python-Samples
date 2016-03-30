class AccountBalance(object):
    def processTransaction(self,startingBalance,transactions):
        for i in range(len(transactions)):
            for j in range(len(transactions[i])):
                if transactions[i][0]=='C':
                    #print transactions[i][0],"VV"
                    y=int(transactions[i][2:])
                    startingBalance+=y
                    break
                elif transactions[i][0]=='D':
                    #print transactions[i][0],"XX"
                    y=int(transactions[i][2:])
                    startingBalance-=y
                    break
        return startingBalance
                #print transactions[i][j]
               
            #print i
x=AccountBalance()
print x.processTransaction((53874),("D 1234", "C 987", "D 2345", "C 654", "D 6789", "D 34567"))
        
