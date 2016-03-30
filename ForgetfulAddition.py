class ForgetfulAddition(object):
    def minNumber(self,expression):
        s=[]
        expression=list(expression)
        print expression
        for i in range(1,len(expression)):
            #print "mmm"
            #s.append(expression[i])
            s.append(int(''.join(expression[:i]))+int(''.join(expression[i:])))
        return min(s)
x=ForgetfulAddition()
print x.minNumber("22")
