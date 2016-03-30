class TopFox(object):
    def possibleHandles(self,familyName,givenName):
        count=0
        l=[]
        for i in range(len(familyName)):
            b=familyName[:i+1]
            print b
            for j in range(len(givenName)):
                d=b+givenName[:j+1]
                #l.append(b+givenName[:j+1])
                if not d in l:
                    print "xx"
                    l.append(b+givenName[:j+1])
                    count+=1
        return count
                print l
        print count
x=TopFox()
print x.possibleHandles(("ab"),("cd"))
