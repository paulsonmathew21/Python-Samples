class MiddleCode(object):
    def encode(self,s):
        t=[]
        s=list(s)
        print s
        while len(s)>0:
            if len(s)%2==0:
                print " X"
                if ord(s[len(s)/2]) <= ord(s[(len(s)/2)-1]):
                    print "  Y"
                    t.append(s[len(s)/2])
                    
                    print "   ",len(s)/2
                    print "    ",s[len(s)/2]
                    del s[len(s)/2]
                    print s
                    #break
                else:
                    t.append(s[(len(s)/2)-1])
                    print "   ",len(s)/2-1
                    print "    ",s[(len(s)/2)-1]
                    del s[(len(s)/2)-1]
                    print s
                #break
            else:
                t.append(s[len(s)/2])
                print len(s)/2
                print s[len(s)/2]
                del s[len(s)/2]
                print s
        return ''.join(t)
x=MiddleCode()
print x.encode(("abacaba"))
