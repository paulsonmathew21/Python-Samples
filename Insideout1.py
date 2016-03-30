class InsideOut(object):
    def unscramble(self,line):
        #self.line=line
        #line= list(line)
        #x=len(line)/2
        #print x,len(line)
        r=s=""
        #r+=line[:]
        #r+=line[0,x]
        #r+=line[len(line)/2:]
        #r+=line[0:len(line)/2]
        for i in range(len(line)/2,len(line)):
            r+=line[i]
        for i in range(0,len(line)/2):
            r+=line[i]
        for i in range(len(r)-1,-1,-1):
            s+=r[i]
        return s
x=InsideOut()
print x.unscramble(("I ENIL SIHTHSIREBBIG S"))
