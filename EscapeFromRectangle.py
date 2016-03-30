class EscapeFromRectangle(object):
    def shortest(self,x,y,w,h):
        p=min([x,abs(x-w)])
        print p
        q=min([y,abs(y-h)])
        print q
        return min([p,q])
z=EscapeFromRectangle()
print z.shortest(1,1,5,5)
