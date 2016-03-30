class KiloMan(object):
    def hitsTaken(self,pattern,jumps):
        hit=0
        for i in range(len(pattern)):
            if pattern[i]<=2 and jumps[i]=='S':
                hit+=1
            elif pattern[i]>2 and jumps[i]=='J':
                hit+=1
        return hit
x=KiloMan()
print x.hitsTaken(("132331221"),("JJSSSJSSJ"))
