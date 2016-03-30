class OneDimensionalRobotEasy(object):
    def finalPosition(self,commands,A,B):
        pos=0
        count =0
        for i in commands:
            if i=='R' and pos<=B:
                pos+=1
                
                count+=1
            elif i=='L' and pos>=-A:
                pos-=1
                count+=1
            print pos
        return count
x=OneDimensionalRobotEasy()
print x.finalPosition(("RRLRRLLR"),(10),(10))
