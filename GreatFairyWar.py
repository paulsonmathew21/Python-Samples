class GreatFairyWar(object):
    def minHP(self,dps,hp):
        count=0
        i=0
        while i<=len(hp)-1:
            count+= hp[i]*sum(dps[i:])
            i+=1
            print count
        return count
x=GreatFairyWar()
print x.minHP((1,2),(3,4))
