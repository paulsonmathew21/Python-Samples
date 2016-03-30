class InsideOut(object):
    def unscramble(self,line):
        #self.line=line
        #line= list(line)
        #x=len(line)/2
        #print x,len(line)
        r=""
        #r+=line[:]
        #r+=line[0,x]
        r+=line[len(line)/2:]
        r+=line[0:len(line)/2]
        return r[::-1]
x=InsideOut()
print x.unscramble(("I ENIL SIHTHSIREBBIG S"))
