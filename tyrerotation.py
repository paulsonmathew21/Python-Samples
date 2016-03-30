class TireRotation(object):
    def getCycle(self,initial,current):
        l=str(initial[0]+initial[1]+initial[2]+initial[3])
        #print l
        m=str(initial[3]+initial[2]+initial[0]+initial[1])
        #print m
        n=str(initial[1]+initial[0]+initial[3]+initial[2])
        #print n
        o=str(initial[2]+initial[3]+initial[1]+initial[0])
        #print o
        if current==l:
            return 1
        elif current==m:
            return 2
        elif current==n:
            return 3
        elif current==o:
            return 4
        else:
            return -1
                 
x=TireRotation()
print x.getCycle(("ZAXN"),("XNAZ"))
        
