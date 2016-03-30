class AlienAndPassword(object):
    def getNumber(self,s):
        c=1
        for i in range(0,len(s)-1):
            if i+1!=len(s):
                if s[i]!=s[i+1]:
                    c+=1
                    
        return c
x=AlienAndPassword()
print x.getNumber("AGAAGAHHHHFTQLLAPUURQQRRRUFJJSBSZVJZZZ")
