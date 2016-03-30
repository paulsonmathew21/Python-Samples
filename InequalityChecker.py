class InequalityChecker(object):
    def getDifferences(self,n):
        s=0
        for i in range(1,n):
            s+=i**3
        print "ss",s
        S=s+(n**3)
        print "S",S
        num=2*(S+s)-(n**4)
        den=4
        if num%den==0:
            print "xxx"
            num=num/den
            den =1
        else:
            while num%2==0 and den%2==0:
                num/=2
                den/=2
        return num,den
x=InequalityChecker()
print x.getDifferences(2)
